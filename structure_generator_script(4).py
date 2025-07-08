#!/usr/bin/env python3
"""
PRISM Carbon Registry Platform - Structure Generator Script
This script creates the complete modular file structure with basic implementations.

Usage: python generate_structure.py [project_name]
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Any

class StructureGenerator:
    def __init__(self, project_name: str = "prism-carbon-registry"):
        self.project_name = project_name
        self.base_path = Path(project_name)
        
    def create_structure(self):
        """Create the complete project structure"""
        print(f"Creating PRISM Carbon Registry structure: {self.project_name}")
        
        # Create all directories
        self._create_directories()
        
        # Create all files
        self._create_root_files()
        self._create_shared_packages()
        self._create_services()
        self._create_frontend()
        self._create_infrastructure()
        self._create_tools()
        self._create_documentation()
        self._create_tests()
        self._create_github_workflows()
        
        print(f"\n✅ Structure created successfully!")
        print(f"📁 Project location: {self.base_path.absolute()}")
        print(f"\nNext steps:")
        print(f"1. cd {self.project_name}")
        print(f"2. docker-compose up -d")
        print(f"3. ./tools/scripts/setup.sh")
        
    def _create_directories(self):
        """Create all necessary directories"""
        directories = [
            # Root level
            "",
            
            # Shared packages
            "packages/common/database",
            "packages/common/models", 
            "packages/common/auth",
            "packages/common/messaging",
            "packages/common/config",
            "packages/common/exceptions",
            "packages/common/logging",
            "packages/common/utils",
            "packages/blockchain/hedera",
            "packages/blockchain/contracts",
            "packages/blockchain/interfaces",
            
            # Services
            "services/api-gateway/app/middleware",
            "services/api-gateway/app/routing",
            "services/api-gateway/app/auth",
            "services/api-gateway/config",
            
            # User service
            "services/user-service/app/domain/entities",
            "services/user-service/app/domain/services", 
            "services/user-service/app/domain/repositories",
            "services/user-service/app/domain/exceptions",
            "services/user-service/app/infrastructure/database/repositories",
            "services/user-service/app/infrastructure/database/migrations",
            "services/user-service/app/infrastructure/external",
            "services/user-service/app/infrastructure/messaging",
            "services/user-service/app/application/commands",
            "services/user-service/app/application/queries",
            "services/user-service/app/application/dto",
            "services/user-service/app/application/events",
            "services/user-service/app/presentation/api/v1/routes",
            "services/user-service/app/presentation/api/v1/schemas",
            "services/user-service/app/presentation/api/middleware",
            "services/user-service/app/presentation/events",
            "services/user-service/tests/unit",
            "services/user-service/tests/integration",
            "services/user-service/alembic",
            
            # Project service
            "services/project-service/app/domain/entities",
            "services/project-service/app/domain/services",
            "services/project-service/app/domain/repositories", 
            "services/project-service/app/infrastructure/database",
            "services/project-service/app/infrastructure/file_storage",
            "services/project-service/app/infrastructure/ai",
            "services/project-service/app/application/commands",
            "services/project-service/app/application/queries",
            "services/project-service/app/application/dto",
            "services/project-service/app/presentation/api/v1/routes",
            "services/project-service/app/presentation/api/v1/schemas",
            "services/project-service/tests",
            
            # Validation service
            "services/validation-service/app/domain/entities",
            "services/validation-service/app/domain/services",
            "services/validation-service/app/domain/repositories",
            "services/validation-service/app/infrastructure/ai",
            "services/validation-service/app/infrastructure/blockchain",
            "services/validation-service/app/application",
            "services/validation-service/app/presentation",
            "services/validation-service/tests",
            
            # Registry service
            "services/registry-service/app/domain/entities",
            "services/registry-service/app/domain/services", 
            "services/registry-service/app/domain/repositories",
            "services/registry-service/app/infrastructure/blockchain",
            "services/registry-service/app/infrastructure/ipfs",
            "services/registry-service/app/application",
            "services/registry-service/app/presentation",
            "services/registry-service/tests",
            
            # Exchange service
            "services/exchange-service/app/domain/entities",
            "services/exchange-service/app/domain/services",
            "services/exchange-service/app/domain/repositories",
            "services/exchange-service/app/infrastructure/matching",
            "services/exchange-service/app/infrastructure/websockets",
            "services/exchange-service/app/application",
            "services/exchange-service/app/presentation",
            "services/exchange-service/tests",
            
            # dMRV service
            "services/dmrv-service/app/domain/entities",
            "services/dmrv-service/app/domain/services",
            "services/dmrv-service/app/domain/repositories",
            "services/dmrv-service/app/infrastructure/satellite",
            "services/dmrv-service/app/infrastructure/iot",
            "services/dmrv-service/app/infrastructure/gis",
            "services/dmrv-service/app/infrastructure/ml",
            "services/dmrv-service/app/application",
            "services/dmrv-service/app/presentation",
            "services/dmrv-service/tests",
            
            # Governance service
            "services/governance-service/app/domain/entities",
            "services/governance-service/app/domain/services",
            "services/governance-service/app/domain/repositories",
            "services/governance-service/app/infrastructure",
            "services/governance-service/app/application",
            "services/governance-service/app/presentation",
            "services/governance-service/tests",
            
            # Notification service
            "services/notification-service/app/domain",
            "services/notification-service/app/infrastructure/email",
            "services/notification-service/app/infrastructure/sms",
            "services/notification-service/app/infrastructure/push",
            "services/notification-service/app/application",
            "services/notification-service/app/presentation",
            "services/notification-service/tests",
            
            # File service
            "services/file-service/app/domain/entities",
            "services/file-service/app/domain/services",
            "services/file-service/app/domain/repositories",
            "services/file-service/app/infrastructure/storage",
            "services/file-service/app/infrastructure/processing",
            "services/file-service/app/infrastructure/security",
            "services/file-service/app/application",
            "services/file-service/app/presentation",
            "services/file-service/tests",
            
            # Frontend
            "frontend/web-app/public",
            "frontend/web-app/src/components/common",
            "frontend/web-app/src/components/forms",
            "frontend/web-app/src/components/charts",
            "frontend/web-app/src/components/tables",
            "frontend/web-app/src/pages/public",
            "frontend/web-app/src/pages/dashboard",
            "frontend/web-app/src/pages/projects",
            "frontend/web-app/src/pages/validation",
            "frontend/web-app/src/pages/registry",
            "frontend/web-app/src/pages/exchange",
            "frontend/web-app/src/pages/admin",
            "frontend/web-app/src/services/api",
            "frontend/web-app/src/services/auth",
            "frontend/web-app/src/services/websockets",
            "frontend/web-app/src/hooks",
            "frontend/web-app/src/context",
            "frontend/web-app/src/utils",
            "frontend/web-app/src/types",
            "frontend/web-app/src/constants",
            "frontend/web-app/src/assets",
            "frontend/web-app/tests",
            "frontend/web-app/build",
            
            "frontend/mobile-app/android",
            "frontend/mobile-app/ios", 
            "frontend/mobile-app/src",
            "frontend/mobile-app/tests",
            
            "frontend/admin-panel/src",
            "frontend/admin-panel/tests",
            
            # Infrastructure
            "infrastructure/kubernetes/base",
            "infrastructure/kubernetes/overlays/development",
            "infrastructure/kubernetes/overlays/staging", 
            "infrastructure/kubernetes/overlays/production",
            "infrastructure/kubernetes/charts",
            "infrastructure/terraform/modules",
            "infrastructure/terraform/environments",
            "infrastructure/docker/base",
            "infrastructure/docker/production",
            "infrastructure/monitoring/prometheus",
            "infrastructure/monitoring/grafana",
            "infrastructure/monitoring/alertmanager",
            
            # Tools
            "tools/scripts",
            "tools/generators",
            "tools/linting",
            "tools/testing",
            
            # Documentation
            "docs/api",
            "docs/architecture", 
            "docs/deployment",
            "docs/user-guides",
            "docs/development",
            
            # Tests
            "tests/integration",
            "tests/e2e",
            "tests/performance",
            "tests/fixtures",
            
            # GitHub
            ".github/workflows",
        ]
        
        for directory in directories:
            path = self.base_path / directory
            path.mkdir(parents=True, exist_ok=True)
            
        print(f"📁 Created {len(directories)} directories")
        
    def _create_root_files(self):
        """Create root level files"""
        files = {
            "README.md": self._get_main_readme(),
            ".gitignore": self._get_gitignore(),
            ".env.example": self._get_env_example(),
            "docker-compose.yml": self._get_docker_compose(),
            "docker-compose.prod.yml": self._get_docker_compose_prod(),
            "Makefile": self._get_makefile(),
            "requirements.txt": "# Root level requirements for development tools\npytest>=7.0.0\nblack>=22.0.0\nflake8>=4.0.0\nmypy>=0.910\npre-commit>=2.15.0",
        }
        
        for filename, content in files.items():
            self._write_file("", filename, content)
            
    def _create_shared_packages(self):
        """Create shared packages"""
        
        # Common package files
        common_files = {
            "packages/common/__init__.py": "",
            "packages/common/database/__init__.py": "",
            "packages/common/database/base.py": self._get_database_base(),
            "packages/common/database/session.py": self._get_database_session(),
            "packages/common/database/utils.py": self._get_database_utils(),
            "packages/common/models/__init__.py": "",
            "packages/common/models/base.py": self._get_models_base(),
            "packages/common/models/user.py": self._get_user_model(),
            "packages/common/models/project.py": self._get_project_model(),
            "packages/common/models/enums.py": self._get_enums(),
            "packages/common/auth/__init__.py": "",
            "packages/common/auth/jwt_handler.py": self._get_jwt_handler(),
            "packages/common/auth/middleware.py": self._get_auth_middleware(),
            "packages/common/auth/decorators.py": self._get_auth_decorators(),
            "packages/common/messaging/__init__.py": "",
            "packages/common/messaging/event_bus.py": self._get_event_bus(),
            "packages/common/messaging/message_types.py": self._get_message_types(),
            "packages/common/messaging/publishers.py": self._get_publishers(),
            "packages/common/config/__init__.py": "",
            "packages/common/config/settings.py": self._get_settings(),
            "packages/common/config/environment.py": self._get_environment(),
            "packages/common/exceptions/__init__.py": "",
            "packages/common/exceptions/base.py": self._get_exceptions_base(),
            "packages/common/exceptions/business.py": self._get_business_exceptions(),
            "packages/common/exceptions/handlers.py": self._get_exception_handlers(),
            "packages/common/logging/__init__.py": "",
            "packages/common/logging/setup.py": self._get_logging_setup(),
            "packages/common/logging/formatters.py": self._get_logging_formatters(),
            "packages/common/logging/middleware.py": self._get_logging_middleware(),
            "packages/common/utils/__init__.py": "",
            "packages/common/utils/validation.py": self._get_validation_utils(),
            "packages/common/utils/serialization.py": self._get_serialization_utils(),
            "packages/common/utils/helpers.py": self._get_helper_utils(),
        }
        
        # Blockchain package files
        blockchain_files = {
            "packages/blockchain/__init__.py": "",
            "packages/blockchain/hedera/__init__.py": "",
            "packages/blockchain/hedera/client.py": self._get_hedera_client(),
            "packages/blockchain/hedera/contracts.py": self._get_hedera_contracts(),
            "packages/blockchain/hedera/utils.py": self._get_hedera_utils(),
            "packages/blockchain/contracts/CarbonAssetToken.sol": self._get_carbon_token_contract(),
            "packages/blockchain/interfaces/__init__.py": "",
            "packages/blockchain/interfaces/registry.py": self._get_registry_interface(),
        }
        
        all_files = {**common_files, **blockchain_files}
        
        for filepath, content in all_files.items():
            path_parts = filepath.split("/")
            directory = "/".join(path_parts[:-1])
            filename = path_parts[-1]
            self._write_file(directory, filename, content)
            
    def _create_services(self):
        """Create all microservices"""
        services = [
            "api-gateway", "user-service", "project-service", 
            "validation-service", "registry-service", "exchange-service",
            "dmrv-service", "governance-service", "notification-service", "file-service"
        ]
        
        for service in services:
            self._create_service(service)
            
    def _create_service(self, service_name: str):
        """Create a single service with all necessary files"""
        service_path = f"services/{service_name}"
        
        # Basic service files
        files = {
            "Dockerfile": self._get_service_dockerfile(service_name),
            "requirements.txt": self._get_service_requirements(service_name),
            "app/__init__.py": "",
            "app/main.py": self._get_service_main(service_name),
            "tests/__init__.py": "",
            "tests/conftest.py": self._get_test_conftest(),
            "tests/unit/__init__.py": "",
            "tests/integration/__init__.py": "",
        }
        
        # Add service-specific files based on service type
        if service_name == "user-service":
            files.update(self._get_user_service_files())
        elif service_name == "project-service":
            files.update(self._get_project_service_files())
        elif service_name == "api-gateway":
            files.update(self._get_api_gateway_files())
        
        for filepath, content in files.items():
            path_parts = filepath.split("/")
            directory = "/".join([service_path] + path_parts[:-1])
            filename = path_parts[-1]
            self._write_file(directory, filename, content)
            
    def _create_frontend(self):
        """Create frontend applications"""
        
        # Web app files
        web_files = {
            "package.json": self._get_frontend_package_json(),
            "Dockerfile": self._get_frontend_dockerfile(),
            "public/index.html": self._get_frontend_index_html(),
            "src/index.tsx": self._get_frontend_index_tsx(),
            "src/App.tsx": self._get_frontend_app_tsx(),
            "src/components/common/Button.tsx": self._get_button_component(),
            "src/components/common/Modal.tsx": self._get_modal_component(),
            "src/pages/public/HomePage.tsx": self._get_home_page(),
            "src/pages/dashboard/DashboardPage.tsx": self._get_dashboard_page(),
            "src/services/api/client.ts": self._get_api_client(),
            "src/services/auth/authService.ts": self._get_auth_service(),
            "src/hooks/useAuth.ts": self._get_use_auth_hook(),
            "src/context/AuthContext.tsx": self._get_auth_context(),
            "src/types/index.ts": self._get_frontend_types(),
            "src/constants/index.ts": self._get_frontend_constants(),
            "tests/setup.ts": self._get_frontend_test_setup(),
        }
        
        for filepath, content in web_files.items():
            path_parts = filepath.split("/")
            directory = "/".join(["frontend/web-app"] + path_parts[:-1])
            filename = path_parts[-1]
            self._write_file(directory, filename, content)
            
    def _create_infrastructure(self):
        """Create infrastructure files"""
        
        infra_files = {
            # Kubernetes
            "kubernetes/base/namespace.yaml": self._get_k8s_namespace(),
            "kubernetes/base/configmap.yaml": self._get_k8s_configmap(),
            "kubernetes/overlays/development/kustomization.yaml": self._get_k8s_kustomization_dev(),
            
            # Terraform
            "terraform/main.tf": self._get_terraform_main(),
            "terraform/variables.tf": self._get_terraform_variables(),
            "terraform/outputs.tf": self._get_terraform_outputs(),
            
            # Monitoring
            "monitoring/prometheus/prometheus.yml": self._get_prometheus_config(),
            "monitoring/grafana/dashboard.json": self._get_grafana_dashboard(),
        }
        
        for filepath, content in infra_files.items():
            path_parts = filepath.split("/")
            directory = "/".join(["infrastructure"] + path_parts[:-1])
            filename = path_parts[-1]
            self._write_file(directory, filename, content)
            
    def _create_tools(self):
        """Create development tools"""
        
        tools_files = {
            "scripts/setup.sh": self._get_setup_script(),
            "scripts/build.sh": self._get_build_script(),
            "scripts/deploy.sh": self._get_deploy_script(),
            "scripts/test.sh": self._get_test_script(),
            "scripts/migrate.sh": self._get_migrate_script(),
            "linting/pyproject.toml": self._get_pyproject_toml(),
            "linting/.flake8": self._get_flake8_config(),
            "testing/pytest.ini": self._get_pytest_config(),
        }
        
        for filepath, content in tools_files.items():
            path_parts = filepath.split("/")
            directory = "/".join(["tools"] + path_parts[:-1])
            filename = path_parts[-1]
            self._write_file(directory, filename, content)
            
    def _create_documentation(self):
        """Create documentation files"""
        
        docs_files = {
            "README.md": self._get_docs_readme(),
            "architecture/overview.md": self._get_architecture_overview(),
            "architecture/services.md": self._get_services_architecture(),
            "deployment/local.md": self._get_local_deployment(),
            "deployment/production.md": self._get_production_deployment(),
            "development/getting-started.md": self._get_getting_started(),
            "development/contributing.md": self._get_contributing_guide(),
            "api/openapi.yml": self._get_openapi_spec(),
        }
        
        for filepath, content in docs_files.items():
            path_parts = filepath.split("/")
            directory = "/".join(["docs"] + path_parts[:-1])
            filename = path_parts[-1]
            self._write_file(directory, filename, content)
            
    def _create_tests(self):
        """Create test files"""
        
        test_files = {
            "integration/test_user_flow.py": self._get_integration_test(),
            "e2e/test_project_creation.py": self._get_e2e_test(),
            "performance/test_load.py": self._get_performance_test(),
            "fixtures/sample_data.json": self._get_test_fixtures(),
        }
        
        for filepath, content in test_files.items():
            path_parts = filepath.split("/")
            directory = "/".join(["tests"] + path_parts[:-1])
            filename = path_parts[-1]
            self._write_file(directory, filename, content)
            
    def _create_github_workflows(self):
        """Create GitHub Actions workflows"""
        
        workflow_files = {
            "ci.yml": self._get_ci_workflow(),
            "cd.yml": self._get_cd_workflow(),
            "security.yml": self._get_security_workflow(),
            "release.yml": self._get_release_workflow(),
        }
        
        for filename, content in workflow_files.items():
            self._write_file(".github/workflows", filename, content)
            
        # Additional GitHub files
        self._write_file(".github", "PULL_REQUEST_TEMPLATE.md", self._get_pr_template())
        
    def _write_file(self, directory: str, filename: str, content: str):
        """Write content to a file"""
        if directory:
            file_path = self.base_path / directory / filename
        else:
            file_path = self.base_path / filename
            
        # Create directory if it doesn't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Content generation methods
    def _get_main_readme(self) -> str:
        return '''# PRISM Carbon Registry Platform

A comprehensive, modular system for end-to-end carbon credit management with AI-powered validation, blockchain-based registry, and automated monitoring.

## Architecture

This platform follows a microservices architecture with the following key principles:
- **Domain-Driven Design (DDD)** for clear business boundaries
- **Clean Architecture** for maintainable, testable code
- **Event-Driven Architecture** for loose coupling
- **CQRS** for optimized read/write operations

## Services

- **API Gateway**: Request routing, authentication, rate limiting
- **User Service**: User management and authentication
- **Project Service**: Carbon project management and documentation
- **Validation Service**: AI-powered project validation and verification
- **Registry Service**: Blockchain-based carbon credit registry
- **Exchange Service**: Carbon credit trading platform
- **dMRV Service**: Digital monitoring, reporting, and verification
- **Governance Service**: Compliance and policy management
- **Notification Service**: Multi-channel notifications
- **File Service**: Secure file storage and processing

## Quick Start

1. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd prism-carbon-registry
   cp .env.example .env
   ```

2. **Start infrastructure**:
   ```bash
   docker-compose up -d
   ```

3. **Initialize services**:
   ```bash
   ./tools/scripts/setup.sh
   ```

4. **Run migrations**:
   ```bash
   ./tools/scripts/migrate.sh
   ```

5. **Access the platform**:
   - Web App: http://localhost:3000
   - API Gateway: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Development

See [Development Guide](docs/development/getting-started.md) for detailed setup instructions.

## Documentation

- [Architecture Overview](docs/architecture/overview.md)
- [Services Documentation](docs/architecture/services.md)
- [API Documentation](docs/api/)
- [Deployment Guides](docs/deployment/)

## Contributing

Please read our [Contributing Guide](docs/development/contributing.md) before submitting pull requests.

## License

[Your License Here]
'''

    def _get_gitignore(self) -> str:
        return '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Database
*.db
*.sqlite
*.sqlite3

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# React
/build
/coverage

# Environment files
.env.local
.env.development.local
.env.test.local
.env.production.local

# Docker
docker-compose.override.yml

# Kubernetes secrets
*-secret.yaml

# Terraform
*.tfstate
*.tfstate.*
.terraform/
.terraform.lock.hcl

# Test coverage
.coverage
htmlcov/
.pytest_cache/

# Blockchain
contracts/build/
.openzeppelin/

# IDE
*.code-workspace
'''

    def _get_env_example(self) -> str:
        return '''# Database Configuration
DATABASE_URL=postgresql://prism:prism_password@localhost:5432/prism_core
MONGO_URL=mongodb://localhost:27017/prism

# Redis
REDIS_URL=redis://localhost:6379

# JWT Configuration
JWT_SECRET=your-jwt-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Hedera Configuration
HEDERA_ACCOUNT_ID=0.0.123456
HEDERA_PRIVATE_KEY=your-hedera-private-key
HEDERA_NETWORK=testnet

# API Keys
OPENAI_API_KEY=your-openai-api-key
SATELLITE_API_KEY=your-satellite-data-api-key

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# File Storage
FILE_STORAGE_TYPE=local  # local, s3, gcs
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_BUCKET_NAME=your-s3-bucket

# External Services
VERRA_API_URL=https://registry.verra.org/api
GOLD_STANDARD_API_URL=https://registry.goldstandard.org/api

# Monitoring
SENTRY_DSN=your-sentry-dsn
PROMETHEUS_PORT=9090

# Development
DEBUG=true
LOG_LEVEL=DEBUG
'''

    def _get_docker_compose(self) -> str:
        return '''version: "3.9"

services:
  # Databases
  postgres:
    image: postgis/postgis:15-3.3-alpine
    container_name: prism_postgres
    environment:
      POSTGRES_USER: prism
      POSTGRES_PASSWORD: prism_password
      POSTGRES_DB: prism_core
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - prism_network

  mongodb:
    image: mongo:6.0
    container_name: prism_mongodb
    environment:
      MONGO_INITDB_DATABASE: prism
    volumes:
      - mongodb_data:/data/db
    ports:
      - "27017:27017"
    networks:
      - prism_network

  redis:
    image: redis:7-alpine
    container_name: prism_redis
    ports:
      - "6379:6379"
    networks:
      - prism_network

  # Services
  api-gateway:
    build: ./services/api-gateway
    container_name: prism_api_gateway
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://prism:prism_password@postgres:5432/prism_core
      - REDIS_URL=redis://redis:6379
    depends_on:
      - postgres
      - redis
    networks:
      - prism_network

  user-service:
    build: ./services/user-service
    container_name: prism_user_service
    ports:
      - "8001:8000"
    environment:
      - DATABASE_URL=postgresql://prism:prism_password@postgres:5432/prism_core
      - REDIS_URL=redis://redis:6379
    depends_on:
      - postgres
      - redis
    networks:
      - prism_network

  project-service:
    build: ./services/project-service
    container_name: prism_project_service
    ports:
      - "8002:8000"
    environment:
      - DATABASE_URL=postgresql://prism:prism_password@postgres:5432/prism_core
      - MONGO_URL=mongodb://mongodb:27017/prism
    depends_on:
      - postgres
      - mongodb
    networks:
      - prism_network

  # Frontend
  web-app:
    build: ./frontend/web-app
    container_name: prism_web_app
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
    depends_on:
      - api-gateway
    networks:
      - prism_network

  # Monitoring
  prometheus:
    image: prom/prometheus:latest
    container_name: prism_prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./infrastructure/monitoring/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - prism_network

  grafana:
    image: grafana/grafana:latest
    container_name: prism_grafana
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - prism_network

networks:
  prism_network:
    driver: bridge

volumes:
  postgres_data:
  mongodb_data:
  grafana_data:
'''

    def _get_docker_compose_prod(self) -> str:
        return '''version: "3.9"

services:
  # Production configuration with health checks, resource limits, etc.
  postgres:
    image: postgis/postgis:15-3.3-alpine
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 1G
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - prism_network

  # Add other production services...

networks:
  prism_network:
    external: true

volumes:
  postgres_data:
    external: true
'''

    def _get_makefile(self) -> str:
        return '''# PRISM Carbon Registry Platform Makefile

.PHONY: help setup build test lint clean deploy

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $1, $2}'

setup: ## Setup development environment
	@echo "Setting up development environment..."
	./tools/scripts/setup.sh

build: ## Build all services
	@echo "Building all services..."
	./tools/scripts/build.sh

test: ## Run all tests
	@echo "Running tests..."
	./tools/scripts/test.sh

lint: ## Run linting
	@echo "Running linters..."
	black --check .
	flake8 .
	mypy .

format: ## Format code
	@echo "Formatting code..."
	black .
	isort .

clean: ## Clean up containers and volumes
	@echo "Cleaning up..."
	docker-compose down -v
	docker system prune -f

migrate: ## Run database migrations
	@echo "Running migrations..."
	./tools/scripts/migrate.sh

deploy-dev: ## Deploy to development
	@echo "Deploying to development..."
	./tools/scripts/deploy.sh dev

deploy-prod: ## Deploy to production
	@echo "Deploying to production..."
	./tools/scripts/deploy.sh prod

logs: ## Show logs
	docker-compose logs -f

up: ## Start all services
	docker-compose up -d

down: ## Stop all services
	docker-compose down

restart: ## Restart all services
	docker-compose restart
'''

    def _get_database_base(self) -> str:
        return '''"""
Base database configuration and utilities
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from typing import Optional

# Database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://prism:prism_password@localhost:5432/prism_core")

# SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    echo=os.getenv("DB_ECHO", "false").lower() == "true"
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Metadata
metadata = MetaData()

def get_db():
    """
    Dependency to get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
    Create all tables
    """
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """
    Drop all tables
    """
    Base.metadata.drop_all(bind=engine)
'''

    def _get_database_session(self) -> str:
        return '''"""
Database session management
"""

from contextlib import contextmanager
from sqlalchemy.orm import Session
from .base import SessionLocal
import logging

logger = logging.getLogger(__name__)

@contextmanager
def get_db_session():
    """
    Context manager for database sessions
    """
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Database session error: {e}")
        raise
    finally:
        session.close()

class DatabaseSession:
    """
    Database session wrapper
    """
    
    def __init__(self):
        self.session: Session = SessionLocal()
    
    def __enter__(self):
        return self.session
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
'''

    def _get_database_utils(self) -> str:
        return '''"""
Database utility functions
"""

from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Any, Dict, List
import logging

logger = logging.getLogger(__name__)

def execute_raw_sql(session: Session, query: str, params: Dict[str, Any] = None) -> List[Dict]:
    """
    Execute raw SQL query
    """
    try:
        result = session.execute(text(query), params or {})
        return [dict(row) for row in result]
    except Exception as e:
        logger.error(f"Error executing raw SQL: {e}")
        raise

def check_table_exists(session: Session, table_name: str) -> bool:
    """
    Check if table exists
    """
    query = """
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_name = :table_name
    );
    """
    result = session.execute(text(query), {"table_name": table_name})
    return result.scalar()

def get_table_row_count(session: Session, table_name: str) -> int:
    """
    Get row count for a table
    """
    query = f"SELECT COUNT(*) FROM {table_name}"
    result = session.execute(text(query))
    return result.scalar()
'''

    def _get_models_base(self) -> str:
        return '''"""
Base models and mixins
"""

from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.sql import func
from packages.common.database.base import Base
import uuid

class TimestampMixin:
    """
    Mixin for created_at and updated_at timestamps
    """
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class UUIDMixin:
    """
    Mixin for UUID primary key
    """
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

class BaseModel(Base, TimestampMixin, UUIDMixin):
    """
    Base model with common fields
    """
    __abstract__ = True
    
    is_active = Column(Boolean, default=True, nullable=False)
    
    def to_dict(self):
        """
        Convert model to dictionary
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
'''

    def _get_user_model(self) -> str:
        return '''"""
User model
"""

from sqlalchemy import Column, String, Boolean, Enum as SQLEnum
from packages.common.models.base import BaseModel
from packages.common.models.enums import UserRole, UserStatus
import enum

class User(BaseModel):
    """
    User model
    """
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    organization = Column(String(255))
    phone = Column(String(50))
    country = Column(String(100))
    role = Column(SQLEnum(UserRole), default=UserRole.PROJECT_DEVELOPER, nullable=False)
    status = Column(SQLEnum(UserStatus), default=UserStatus.ACTIVE, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    last_login = Column(String)  # Store as ISO string
    
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN
    
    def can_validate_projects(self) -> bool:
        return self.role in [UserRole.VALIDATOR, UserRole.ADMIN]
    
    def can_issue_credits(self) -> bool:
        return self.role in [UserRole.REGISTRY_ADMIN, UserRole.ADMIN]
'''

    def _get_project_model(self) -> str:
        return '''"""
Project model
"""

from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from packages.common.models.base import BaseModel
from packages.common.models.enums import ProjectType, ProjectStatus

class Project(BaseModel):
    """
    Carbon project model
    """
    __tablename__ = "projects"
    
    project_id = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    project_type = Column(SQLEnum(ProjectType), nullable=False)
    methodology = Column(String(100))
    country = Column(String(100), nullable=False)
    region = Column(String(100))
    area_hectares = Column(Float)
    estimated_annual_reduction = Column(Integer)  # tCO2e per year
    total_estimated_reduction = Column(Integer)  # Total tCO2e over project lifetime
    crediting_period_start = Column(String)  # ISO date string
    crediting_period_end = Column(String)    # ISO date string
    status = Column(SQLEnum(ProjectStatus), default=ProjectStatus.DRAFT, nullable=False)
    
    # Foreign keys
    owner_id = Column(String, ForeignKey("users.id"), nullable=False)
    validator_id = Column(String, ForeignKey("users.id"))
    
    # Issued credits tracking
    issued_credits = Column(Integer, default=0)
    available_credits = Column(Integer, default=0)
    retired_credits = Column(Integer, default=0)
    
    # Relationships
    owner = relationship("User", foreign_keys=[owner_id])
    validator = relationship("User", foreign_keys=[validator_id])
    
    def get_status_display(self) -> str:
        return self.status.value.replace("_", " ").title()
    
    def is_editable(self) -> bool:
        return self.status in [ProjectStatus.DRAFT, ProjectStatus.REJECTED]
    
    def can_issue_credits(self) -> bool:
        return self.status == ProjectStatus.REGISTERED
'''

    def _get_enums(self) -> str:
        return '''"""
Common enums used across the platform
"""

from enum import Enum

class UserRole(str, Enum):
    """User roles"""
    ADMIN = "admin"
    PROJECT_DEVELOPER = "project_developer"
    VALIDATOR = "validator"
    AUDITOR = "auditor"
    REGISTRY_ADMIN = "registry_admin"
    TRADER = "trader"
    BUYER = "buyer"

class UserStatus(str, Enum):
    """User status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    PENDING = "pending"

class ProjectType(str, Enum):
    """Carbon project types"""
    FORESTRY = "forestry"
    RENEWABLE_ENERGY = "renewable_energy"
    ENERGY_EFFICIENCY = "energy_efficiency"
    METHANE_CAPTURE = "methane_capture"
    INDUSTRIAL = "industrial"
    AGRICULTURE = "agriculture"
    WASTE_MANAGEMENT = "waste_management"
    TRANSPORT = "transport"
    BLUE_CARBON = "blue_carbon"
    DIRECT_AIR_CAPTURE = "direct_air_capture"

class ProjectStatus(str, Enum):
    """Project status"""
    DRAFT = "draft"
    SUBMITTED = "submitted"
    UNDER_VALIDATION = "under_validation"
    VALIDATED = "validated"
    REJECTED = "rejected"
    REGISTERED = "registered"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    COMPLETED = "completed"

class DocumentType(str, Enum):
    """Document types"""
    PDD = "pdd"
    MONITORING_REPORT = "monitoring_report"
    VALIDATION_REPORT = "validation_report"
    VERIFICATION_REPORT = "verification_report"
    PROJECT_PHOTO = "project_photo"
    SATELLITE_IMAGE = "satellite_image"
    LEGAL_DOCUMENT = "legal_document"
    CERTIFICATE = "certificate"
    OTHER = "other"

class CreditStatus(str, Enum):
    """Carbon credit status"""
    ISSUED = "issued"
    AVAILABLE = "available"
    RESERVED = "reserved"
    TRANSFERRED = "transferred"
    RETIRED = "retired"
    CANCELLED = "cancelled"

class TransactionType(str, Enum):
    """Transaction types"""
    ISSUANCE = "issuance"
    TRANSFER = "transfer"
    RETIREMENT = "retirement"
    CANCELLATION = "cancellation"
'''

    def _get_auth_middleware(self) -> str:
        return '''"""
Authentication middleware for FastAPI
"""

from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
import logging
from .jwt_handler import verify_token

logger = logging.getLogger(__name__)
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get current user from JWT token
    """
    try:
        payload = verify_token(credentials.credentials)
        if payload is None:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
        
        return payload
    except Exception as e:
        logger.error(f"Authentication error: {e}")
        raise HTTPException(status_code=401, detail="Authentication failed")

async def get_current_user_optional(request: Request) -> Optional[dict]:
    """
    Get current user optionally (doesn't raise error if no token)
    """
    try:
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None
        
        token = auth_header.split(" ")[1]
        payload = verify_token(token)
        return payload
    except Exception:
        return None

def require_role(required_role: str):
    """
    Decorator to require specific user role
    """
    def role_checker(current_user: dict = Depends(get_current_user)):
        user_role = current_user.get("role")
        if user_role != required_role:
            raise HTTPException(
                status_code=403, 
                detail=f"Access denied. Required role: {required_role}"
            )
        return current_user
    return role_checker
'''

    def _get_auth_decorators(self) -> str:
        return '''"""
Authentication decorators and utilities
"""

from functools import wraps
from typing import Callable, List, Optional
from fastapi import HTTPException, Depends
from .middleware import get_current_user
import logging

logger = logging.getLogger(__name__)

def authenticated(func: Callable) -> Callable:
    """
    Decorator to require authentication
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # This decorator is used with FastAPI Depends in route definitions
        current_user = kwargs.get('current_user')
        if not current_user:
            raise HTTPException(status_code=401, detail="Authentication required")
        return await func(*args, **kwargs)
    return wrapper

def require_roles(allowed_roles: List[str]):
    """
    Decorator factory to require specific roles
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_user = kwargs.get('current_user')
            if not current_user:
                raise HTTPException(status_code=401, detail="Authentication required")
            
            user_role = current_user.get('role')
            if user_role not in allowed_roles:
                raise HTTPException(
                    status_code=403, 
                    detail=f"Access denied. Required roles: {', '.join(allowed_roles)}"
                )
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def require_permissions(required_permissions: List[str]):
    """
    Decorator factory to require specific permissions
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_user = kwargs.get('current_user')
            if not current_user:
                raise HTTPException(status_code=401, detail="Authentication required")
            
            user_permissions = current_user.get('permissions', [])
            missing_permissions = set(required_permissions) - set(user_permissions)
            
            if missing_permissions:
                raise HTTPException(
                    status_code=403,
                    detail=f"Missing permissions: {', '.join(missing_permissions)}"
                )
            return await func(*args, **kwargs)
        return wrapper
    return decorator
'''

    def _get_jwt_handler(self) -> str:
        return '''"""
JWT token handling utilities
"""

import jwt
import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "24"))

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create JWT access token
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS)
    
    to_encode.update({"exp": expire, "iat": datetime.utcnow()})
    
    try:
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
    except Exception as e:
        logger.error(f"Error creating JWT token: {e}")
        raise

def verify_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Verify and decode JWT token
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        logger.warning("JWT token has expired")
        return None
    except jwt.JWTError as e:
        logger.error(f"JWT verification error: {e}")
        return None

def refresh_token(token: str) -> Optional[str]:
    """
    Refresh JWT token if valid
    """
    payload = verify_token(token)
    if payload:
        # Remove exp and iat from payload
        payload.pop("exp", None)
        payload.pop("iat", None)
        return create_access_token(payload)
    return None
'''

    def _get_message_types(self) -> str:
        return '''"""
Message types for event bus communication
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional
from datetime import datetime
from packages.common.models.enums import ProjectStatus, UserRole

@dataclass
class UserCreatedEvent:
    """Event fired when a new user is created"""
    user_id: str
    email: str
    full_name: str
    role: UserRole
    timestamp: str = datetime.utcnow().isoformat()

@dataclass
class ProjectCreatedEvent:
    """Event fired when a new project is created"""
    project_id: str
    owner_id: str
    project_name: str
    project_type: str
    timestamp: str = datetime.utcnow().isoformat()

@dataclass
class ProjectStatusChangedEvent:
    """Event fired when project status changes"""
    project_id: str
    old_status: ProjectStatus
    new_status: ProjectStatus
    changed_by: str
    timestamp: str = datetime.utcnow().isoformat()

@dataclass
class DocumentUploadedEvent:
    """Event fired when a document is uploaded"""
    project_id: str
    document_id: str
    document_type: str
    uploaded_by: str
    timestamp: str = datetime.utcnow().isoformat()

@dataclass
class ValidationCompletedEvent:
    """Event fired when project validation is completed"""
    project_id: str
    validator_id: str
    validation_result: str  # "approved" or "rejected"
    feedback: Optional[str] = None
    timestamp: str = datetime.utcnow().isoformat()

@dataclass
class CreditsIssuedEvent:
    """Event fired when carbon credits are issued"""
    project_id: str
    credit_batch_id: str
    amount: int
    issued_to: str
    blockchain_tx_hash: str
    timestamp: str = datetime.utcnow().isoformat()

@dataclass
class CreditsTransferredEvent:
    """Event fired when credits are transferred"""
    from_address: str
    to_address: str
    credit_batch_id: str
    amount: int
    blockchain_tx_hash: str
    timestamp: str = datetime.utcnow().isoformat()

@dataclass
class CreditsRetiredEvent:
    """Event fired when credits are retired"""
    retired_by: str
    credit_batch_id: str
    amount: int
    retirement_reason: str
    blockchain_tx_hash: str
    timestamp: str = datetime.utcnow().isoformat()
'''

    def _get_publishers(self) -> str:
        return '''"""
Event publishers for different services
"""

import asyncio
import logging
from typing import Any, Dict
from .event_bus import event_bus, Event
from .message_types import *

logger = logging.getLogger(__name__)

class EventPublisher:
    """Base event publisher"""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
    
    async def publish_event(self, event_type: str, data: Dict[str, Any], correlation_id: str = None):
        """Publish a generic event"""
        event = Event(
            event_type=event_type,
            data=data,
            timestamp=datetime.utcnow().isoformat(),
            source_service=self.service_name,
            correlation_id=correlation_id
        )
        await event_bus.publish(event)

class UserEventPublisher(EventPublisher):
    """Publisher for user-related events"""
    
    def __init__(self):
        super().__init__("user-service")
    
    async def publish_user_created(self, user_data: UserCreatedEvent):
        """Publish user created event"""
        await self.publish_event("user.created", user_data.__dict__)

class ProjectEventPublisher(EventPublisher):
    """Publisher for project-related events"""
    
    def __init__(self):
        super().__init__("project-service")
    
    async def publish_project_created(self, project_data: ProjectCreatedEvent):
        """Publish project created event"""
        await self.publish_event("project.created", project_data.__dict__)
    
    async def publish_project_status_changed(self, status_data: ProjectStatusChangedEvent):
        """Publish project status changed event"""
        await self.publish_event("project.status_changed", status_data.__dict__)
    
    async def publish_document_uploaded(self, document_data: DocumentUploadedEvent):
        """Publish document uploaded event"""
        await self.publish_event("document.uploaded", document_data.__dict__)

class RegistryEventPublisher(EventPublisher):
    """Publisher for registry-related events"""
    
    def __init__(self):
        super().__init__("registry-service")
    
    async def publish_credits_issued(self, credits_data: CreditsIssuedEvent):
        """Publish credits issued event"""
        await self.publish_event("credits.issued", credits_data.__dict__)
    
    async def publish_credits_transferred(self, transfer_data: CreditsTransferredEvent):
        """Publish credits transferred event"""
        await self.publish_event("credits.transferred", transfer_data.__dict__)
    
    async def publish_credits_retired(self, retirement_data: CreditsRetiredEvent):
        """Publish credits retired event"""
        await self.publish_event("credits.retired", retirement_data.__dict__)

class ValidationEventPublisher(EventPublisher):
    """Publisher for validation-related events"""
    
    def __init__(self):
        super().__init__("validation-service")
    
    async def publish_validation_completed(self, validation_data: ValidationCompletedEvent):
        """Publish validation completed event"""
        await self.publish_event("validation.completed", validation_data.__dict__)
'''

    def _get_environment(self) -> str:
        return '''"""
Environment configuration utilities
"""

import os
from enum import Enum
from typing import Optional

class Environment(str, Enum):
    """Environment types"""
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"

def get_environment() -> Environment:
    """Get current environment"""
    env_name = os.getenv("ENVIRONMENT", "development").lower()
    
    try:
        return Environment(env_name)
    except ValueError:
        return Environment.DEVELOPMENT

def is_development() -> bool:
    """Check if running in development"""
    return get_environment() == Environment.DEVELOPMENT

def is_production() -> bool:
    """Check if running in production"""
    return get_environment() == Environment.PRODUCTION

def is_testing() -> bool:
    """Check if running in testing"""
    return get_environment() == Environment.TESTING

def get_log_level() -> str:
    """Get appropriate log level for environment"""
    env = get_environment()
    
    if env == Environment.PRODUCTION:
        return "WARNING"
    elif env == Environment.TESTING:
        return "ERROR"
    else:
        return "DEBUG"

def get_database_echo() -> bool:
    """Get database echo setting for environment"""
    return is_development() and os.getenv("DB_ECHO", "false").lower() == "true"
'''

    def _get_business_exceptions(self) -> str:
        return '''"""
Business-specific exceptions
"""

from .base import BaseException, ErrorCode

# User-related exceptions
class UserNotFoundError(BaseException):
    """User not found error"""
    
    def __init__(self, user_id: str):
        super().__init__(
            message=f"User with ID {user_id} not found",
            error_code=ErrorCode.USER_NOT_FOUND,
            status_code=404
        )

class UserAlreadyExistsError(BaseException):
    """User already exists error"""
    
    def __init__(self, email: str):
        super().__init__(
            message=f"User with email {email} already exists",
            error_code=ErrorCode.USER_ALREADY_EXISTS,
            status_code=409
        )

class InvalidCredentialsError(BaseException):
    """Invalid credentials error"""
    
    def __init__(self):
        super().__init__(
            message="Invalid email or password",
            error_code=ErrorCode.INVALID_CREDENTIALS,
            status_code=401
        )

# Project-related exceptions
class ProjectNotFoundError(BaseException):
    """Project not found error"""
    
    def __init__(self, project_id: str):
        super().__init__(
            message=f"Project with ID {project_id} not found",
            error_code=ErrorCode.PROJECT_NOT_FOUND,
            status_code=404
        )

class ProjectAlreadyExistsError(BaseException):
    """Project already exists error"""
    
    def __init__(self, project_id: str):
        super().__init__(
            message=f"Project with ID {project_id} already exists",
            error_code=ErrorCode.PROJECT_ALREADY_EXISTS,
            status_code=409
        )

class InvalidProjectStatusError(BaseException):
    """Invalid project status transition error"""
    
    def __init__(self, current_status: str, new_status: str):
        super().__init__(
            message=f"Cannot change project status from {current_status} to {new_status}",
            error_code=ErrorCode.INVALID_PROJECT_STATUS,
            status_code=400
        )

# File-related exceptions
class FileNotFoundError(BaseException):
    """File not found error"""
    
    def __init__(self, file_id: str):
        super().__init__(
            message=f"File with ID {file_id} not found",
            error_code=ErrorCode.FILE_NOT_FOUND,
            status_code=404
        )

class FileTooLargeError(BaseException):
    """File too large error"""
    
    def __init__(self, max_size: int):
        super().__init__(
            message=f"File size exceeds maximum allowed size of {max_size} bytes",
            error_code=ErrorCode.FILE_TOO_LARGE,
            status_code=413
        )

class InvalidFileTypeError(BaseException):
    """Invalid file type error"""
    
    def __init__(self, file_type: str, allowed_types: list):
        super().__init__(
            message=f"File type {file_type} not allowed. Allowed types: {', '.join(allowed_types)}",
            error_code=ErrorCode.INVALID_FILE_TYPE,
            status_code=400
        )

# Blockchain-related exceptions
class BlockchainError(BaseException):
    """General blockchain error"""
    
    def __init__(self, message: str = "Blockchain operation failed"):
        super().__init__(
            message=message,
            error_code=ErrorCode.BLOCKCHAIN_ERROR,
            status_code=500
        )

class InsufficientBalanceError(BaseException):
    """Insufficient balance error"""
    
    def __init__(self, required: int, available: int):
        super().__init__(
            message=f"Insufficient balance. Required: {required}, Available: {available}",
            error_code=ErrorCode.INSUFFICIENT_BALANCE,
            status_code=400
        )

class TransactionFailedError(BaseException):
    """Transaction failed error"""
    
    def __init__(self, tx_hash: str, reason: str = "Unknown"):
        super().__init__(
            message=f"Transaction {tx_hash} failed: {reason}",
            error_code=ErrorCode.TRANSACTION_FAILED,
            status_code=500
        )
'''

    def _get_exception_handlers(self) -> str:
        return '''"""
Exception handlers for FastAPI applications
"""

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging
from typing import Union
from .base import BaseException

logger = logging.getLogger(__name__)

async def base_exception_handler(request: Request, exc: BaseException):
    """Handle custom base exceptions"""
    
    logger.error(
        f"Business exception: {exc.error_code.value}",
        extra={
            "error_code": exc.error_code.value,
            "message": exc.message,
            "details": exc.details,
            "path": request.url.path,
            "method": request.method,
        }
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code.value,
            "message": exc.message,
            "details": exc.details,
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle FastAPI validation errors"""
    
    logger.warning(
        f"Validation error on {request.method} {request.url.path}",
        extra={"validation_errors": exc.errors()}
    )
    
    return JSONResponse(
        status_code=422,
        content={
            "error_code": "VALIDATION_ERROR",
            "message": "Validation failed",
            "details": {
                "validation_errors": exc.errors()
            }
        }
    )

async def http_exception_handler(request: Request, exc: Union[HTTPException, StarletteHTTPException]):
    """Handle HTTP exceptions"""
    
    logger.warning(
        f"HTTP exception: {exc.status_code}",
        extra={
            "status_code": exc.status_code,
            "detail": str(exc.detail),
            "path": request.url.path,
            "method": request.method,
        }
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": f"HTTP_{exc.status_code}",
            "message": str(exc.detail),
            "details": {}
        }
    )

async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions"""
    
    logger.error(
        f"Unexpected exception: {type(exc).__name__}",
        extra={
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
            "path": request.url.path,
            "method": request.method,
        },
        exc_info=True
    )
    
    return JSONResponse(
        status_code=500,
        content={
            "error_code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred",
            "details": {}
        }
    )

def setup_exception_handlers(app):
    """Setup exception handlers for a FastAPI app"""
    
    app.add_exception_handler(BaseException, base_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
'''

    def _get_validation_utils(self) -> str:
        return '''"""
Event bus for inter-service communication
"""

import asyncio
import json
import logging
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

@dataclass
class Event:
    """Base event class"""
    event_type: str
    data: Dict[str, Any]
    timestamp: str
    source_service: str
    correlation_id: Optional[str] = None

class EventHandler(ABC):
    """Abstract event handler"""
    
    @abstractmethod
    async def handle(self, event: Event) -> None:
        pass

class EventBus:
    """
    Simple in-memory event bus
    In production, this would be replaced with Redis, RabbitMQ, or Kafka
    """
    
    def __init__(self):
        self._handlers: Dict[str, List[EventHandler]] = {}
        self._subscribers: Dict[str, List[Callable]] = {}
    
    def subscribe(self, event_type: str, handler: Callable):
        """Subscribe to an event type"""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)
    
    async def publish(self, event: Event):
        """Publish an event"""
        logger.info(f"Publishing event: {event.event_type}")
        
        # Call all subscribers
        if event.event_type in self._subscribers:
            for handler in self._subscribers[event.event_type]:
                try:
                    await handler(event)
                except Exception as e:
                    logger.error(f"Error in event handler: {e}")
    
    def register_handler(self, event_type: str, handler: EventHandler):
        """Register an event handler"""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

# Global event bus instance
event_bus = EventBus()
'''

    def _get_service_main(self, service_name: str) -> str:
        return f'''"""
{service_name.replace("-", " ").title()} Service Main Application
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from packages.common.logging.setup import setup_logging
from packages.common.config.settings import get_settings
import logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Get settings
settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title="{service_name.replace("-", " ").title()} Service",
    description="PRISM Carbon Registry - {service_name.replace("-", " ").title()} Service",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {{"message": "{service_name.replace("-", " ").title()} Service is running"}}

@app.get("/health")
async def health_check():
    return {{"status": "healthy", "service": "{service_name}"}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''

    def _get_service_dockerfile(self, service_name: str) -> str:
        return f'''FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''

    def _get_service_requirements(self, service_name: str) -> str:
        base_requirements = '''fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.4.0
sqlalchemy>=2.0.0
alembic>=1.12.0
psycopg2-binary>=2.9.0
redis>=5.0.0
celery>=5.3.0
python-multipart>=0.0.6
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
python-dotenv>=1.0.0
requests>=2.31.0
'''
        
        service_specific = {
            'user-service': 'bcrypt>=4.0.0\nemail-validator>=2.0.0\n',
            'project-service': 'PyPDF2>=3.0.0\nPillow>=10.0.0\nopenai>=1.0.0\n',
            'validation-service': 'scikit-learn>=1.3.0\nnumpy>=1.24.0\n',
            'registry-service': 'web3>=6.0.0\nipfshttpclient>=0.8.0\n',
            'exchange-service': 'websockets>=11.0.0\n',
            'dmrv-service': 'gdal>=3.7.0\nrasterio>=1.3.0\n',
        }
        
        return base_requirements + service_specific.get(service_name, '')

    def _get_user_service_files(self) -> Dict[str, str]:
        return {
            "app/domain/entities/user.py": '''"""User domain entity"""

from dataclasses import dataclass
from typing import Optional
from packages.common.models.enums import UserRole, UserStatus

@dataclass
class UserEntity:
    id: str
    email: str
    full_name: str
    organization: Optional[str]
    role: UserRole
    status: UserStatus
    is_verified: bool
    
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN
''',
            "app/domain/services/user_service.py": '''"""User domain service"""

from typing import Optional
from packages.common.exceptions.business import UserNotFoundError
from ..entities.user import UserEntity
from ..repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    async def create_user(self, user_data: dict) -> UserEntity:
        """Create a new user"""
        return await self.user_repository.create(user_data)
    
    async def get_user_by_email(self, email: str) -> Optional[UserEntity]:
        """Get user by email"""
        return await self.user_repository.get_by_email(email)
    
    async def verify_user(self, user_id: str) -> bool:
        """Verify user account"""
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User {user_id} not found")
        
        return await self.user_repository.update(user_id, {"is_verified": True})
''',
            "app/presentation/api/v1/routes/users.py": '''"""User API routes"""

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schemas.user import UserCreate, UserResponse
from ....domain.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    user_service: UserService = Depends()
):
    """Create a new user"""
    return await user_service.create_user(user_data.dict())

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: str,
    user_service: UserService = Depends()
):
    """Get user by ID"""
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
''',
        }

    def _get_frontend_package_json(self) -> str:
        return '''{
  "name": "prism-web-app",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "@types/jest": "^27.5.2",
    "@types/node": "^16.18.11",
    "@types/react": "^18.0.26",
    "@types/react-dom": "^18.0.10",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.0",
    "react-scripts": "5.0.1",
    "typescript": "^4.9.4",
    "web-vitals": "^2.1.4",
    "axios": "^1.2.2",
    "react-query": "^3.39.3",
    "@mui/material": "^5.11.2",
    "@mui/icons-material": "^5.11.0",
    "@emotion/react": "^11.10.5",
    "@emotion/styled": "^11.10.5",
    "recharts": "^2.4.3"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@types/react-router-dom": "^5.3.3"
  }
}'''

    def _get_setup_script(self) -> str:
        return '''#!/bin/bash

# PRISM Carbon Registry Platform Setup Script

set -e

echo "🚀 Setting up PRISM Carbon Registry Platform..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please update the .env file with your actual configuration values"
fi

# Build and start services
echo "🏗️  Building and starting services..."
docker-compose up -d --build

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 30

# Run database migrations
echo "📊 Running database migrations..."
./tools/scripts/migrate.sh

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend/web-app
npm install
cd ../..

echo "✅ Setup complete!"
echo ""
echo "🌐 Access the platform:"
echo "   - Web App: http://localhost:3000"
echo "   - API Gateway: http://localhost:8000"
echo "   - API Docs: http://localhost:8000/docs"
echo "   - Grafana: http://localhost:3001 (admin/admin)"
echo ""
echo "🔧 Useful commands:"
echo "   - View logs: make logs"
echo "   - Run tests: make test"
echo "   - Stop services: make down"
'''

    def _get_ci_workflow(self) -> str:
        return '''name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run linting
      run: |
        black --check .
        flake8 .
        mypy .
    
    - name: Run tests
      run: |
        pytest --cov=. --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build:
    runs-on: ubuntu-latest
    needs: test
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Login to Container Registry
      uses: docker/login-action@v2
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Build and push images
      run: |
        docker-compose build
        docker-compose push
'''

    def _get_carbon_token_contract(self) -> str:
        return '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title CarbonAssetToken
 * @dev ERC1155 token for carbon credits and project NFTs
 */
contract CarbonAssetToken is ERC1155, Ownable, Pausable {
    
    // Token types
    uint256 public constant PROJECT_NFT = 1;
    uint256 public constant CARBON_CREDIT = 2;
    
    // Mapping from token ID to project metadata URI
    mapping(uint256 => string) private _tokenURIs;
    
    // Mapping from token ID to total supply
    mapping(uint256 => uint256) public totalSupply;
    
    // Events
    event CreditIssued(uint256 indexed tokenId, address indexed to, uint256 amount);
    event CreditRetired(uint256 indexed tokenId, address indexed from, uint256 amount);
    
    constructor(string memory uri) ERC1155(uri) {}
    
    /**
     * @dev Issue carbon credits
     */
    function issueCredits(
        address to,
        uint256 tokenId,
        uint256 amount,
        string memory tokenURI,
        bytes memory data
    ) public onlyOwner {
        _mint(to, tokenId, amount, data);
        totalSupply[tokenId] += amount;
        
        if (bytes(tokenURI).length > 0) {
            _setTokenURI(tokenId, tokenURI);
        }
        
        emit CreditIssued(tokenId, to, amount);
    }
    
    /**
     * @dev Retire carbon credits (burn)
     */
    function retireCredits(uint256 tokenId, uint256 amount) public {
        _burn(msg.sender, tokenId, amount);
        totalSupply[tokenId] -= amount;
        
        emit CreditRetired(tokenId, msg.sender, amount);
    }
    
    /**
     * @dev Set token URI
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }
    
    /**
     * @dev Get token URI
     */
    function uri(uint256 tokenId) public view override returns (string memory) {
        string memory tokenURI = _tokenURIs[tokenId];
        return bytes(tokenURI).length > 0 ? tokenURI : super.uri(tokenId);
    }
    
    /**
     * @dev Pause contract
     */
    function pause() public onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause contract
     */
    function unpause() public onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Override required by Solidity
     */
    function _beforeTokenTransfer(
        address operator,
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(operator, from, to, ids, amounts, data);
    }
}
'''

    def _get_hedera_client(self) -> str:
        return '''"""
Hedera Hashgraph client for blockchain interactions
"""

import os
import json
import logging
from typing import Optional, Dict, Any
from web3 import Web3
from eth_account import Account

logger = logging.getLogger(__name__)

class HederaClient:
    """
    Client for interacting with Hedera Hashgraph
    """
    
    def __init__(self):
        self.network = os.getenv("HEDERA_NETWORK", "testnet")
        self.account_id = os.getenv("HEDERA_ACCOUNT_ID")
        self.private_key = os.getenv("HEDERA_PRIVATE_KEY")
        
        # Web3 connection for EVM operations
        if self.network == "mainnet":
            self.web3_url = "https://mainnet.hashio.io/api"
        else:
            self.web3_url = "https://testnet.hashio.io/api"
            
        self.web3 = Web3(Web3.HTTPProvider(self.web3_url))
        
        # Contract addresses (deploy and update these)
        self.carbon_token_address = os.getenv("CARBON_TOKEN_ADDRESS")
        
    def deploy_carbon_token_contract(self, contract_bytecode: str, abi: list) -> str:
        """
        Deploy the carbon token contract
        """
        try:
            # Create account from private key
            account = Account.from_key(self.private_key)
            
            # Create contract
            contract = self.web3.eth.contract(abi=abi, bytecode=contract_bytecode)
            
            # Build transaction
            transaction = contract.constructor("ipfs://").buildTransaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('20', 'gwei'),
            })
            
            # Sign and send transaction
            signed_txn = self.web3.eth.account.sign_transaction(transaction, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            
            # Wait for receipt
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            logger.info(f"Carbon token contract deployed at: {receipt.contractAddress}")
            return receipt.contractAddress
            
        except Exception as e:
            logger.error(f"Error deploying contract: {e}")
            raise
    
    def issue_carbon_credits(
        self, 
        to_address: str, 
        token_id: int, 
        amount: int, 
        metadata_uri: str
    ) -> str:
        """
        Issue carbon credits to an address
        """
        try:
            if not self.carbon_token_address:
                raise ValueError("Carbon token contract not deployed")
            
            # Load contract ABI (this should be loaded from a file)
            with open("packages/blockchain/contracts/CarbonAssetToken.json", "r") as f:
                contract_data = json.load(f)
                abi = contract_data["abi"]
            
            # Create contract instance
            contract = self.web3.eth.contract(
                address=self.carbon_token_address,
                abi=abi
            )
            
            # Create account from private key
            account = Account.from_key(self.private_key)
            
            # Build transaction
            transaction = contract.functions.issueCredits(
                to_address,
                token_id,
                amount,
                metadata_uri,
                b''
            ).buildTransaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 500000,
                'gasPrice': self.web3.toWei('20', 'gwei'),
            })
            
            # Sign and send transaction
            signed_txn = self.web3.eth.account.sign_transaction(transaction, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            
            logger.info(f"Carbon credits issued. Transaction: {tx_hash.hex()}")
            return tx_hash.hex()
            
        except Exception as e:
            logger.error(f"Error issuing carbon credits: {e}")
            raise
    
    def retire_carbon_credits(self, owner_address: str, token_id: int, amount: int) -> str:
        """
        Retire (burn) carbon credits
        """
        try:
            # Similar implementation to issue_carbon_credits
            # but calling retireCredits function
            pass
            
        except Exception as e:
            logger.error(f"Error retiring carbon credits: {e}")
            raise
    
    def get_credit_balance(self, address: str, token_id: int) -> int:
        """
        Get carbon credit balance for an address
        """
        try:
            if not self.carbon_token_address:
                return 0
            
            # Load contract ABI
            with open("packages/blockchain/contracts/CarbonAssetToken.json", "r") as f:
                contract_data = json.load(f)
                abi = contract_data["abi"]
            
            # Create contract instance
            contract = self.web3.eth.contract(
                address=self.carbon_token_address,
                abi=abi
            )
            
            # Call balanceOf function
            balance = contract.functions.balanceOf(address, token_id).call()
            return balance
            
        except Exception as e:
            logger.error(f"Error getting credit balance: {e}")
            return 0

# Global client instance
hedera_client = HederaClient()
'''

    def _get_settings(self) -> str:
        return '''"""
Application settings and configuration
"""

from pydantic import BaseSettings, validator
from typing import Optional, List
import os

class DatabaseSettings(BaseSettings):
    """Database configuration"""
    url: str = "postgresql://prism:prism_password@localhost:5432/prism_core"
    echo: bool = False
    pool_size: int = 10
    max_overflow: int = 20
    
    class Config:
        env_prefix = "DB_"

class RedisSettings(BaseSettings):
    """Redis configuration"""
    url: str = "redis://localhost:6379"
    
    class Config:
        env_prefix = "REDIS_"

class JWTSettings(BaseSettings):
    """JWT configuration"""
    secret: str = "your-secret-key"
    algorithm: str = "HS256"
    expiration_hours: int = 24
    
    class Config:
        env_prefix = "JWT_"

class HederaSettings(BaseSettings):
    """Hedera blockchain configuration"""
    account_id: Optional[str] = None
    private_key: Optional[str] = None
    network: str = "testnet"
    
    class Config:
        env_prefix = "HEDERA_"

class EmailSettings(BaseSettings):
    """Email configuration"""
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    username: Optional[str] = None
    password: Optional[str] = None
    
    class Config:
        env_prefix = "SMTP_"

class Settings(BaseSettings):
    """Main application settings"""
    
    # Basic settings
    app_name: str = "PRISM Carbon Registry"
    version: str = "1.0.0"
    debug: bool = False
    log_level: str = "INFO"
    
    # Service URLs
    user_service_url: str = "http://localhost:8001"
    project_service_url: str = "http://localhost:8002"
    validation_service_url: str = "http://localhost:8003"
    registry_service_url: str = "http://localhost:8004"
    
    # CORS settings
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:3001"]
    
    # Component settings
    database: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    jwt: JWTSettings = JWTSettings()
    hedera: HederaSettings = HederaSettings()
    email: EmailSettings = EmailSettings()
    
    @validator("cors_origins", pre=True)
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = False

def get_settings() -> Settings:
    """Get application settings"""
    return Settings()
'''

    def _get_exceptions_base(self) -> str:
        return '''"""
Base exception classes and error handling
"""

from enum import Enum
from typing import Optional, Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class ErrorCode(str, Enum):
    """Standard error codes"""
    
    # Generic errors
    INTERNAL_ERROR = "INTERNAL_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    
    # User errors
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_ALREADY_EXISTS = "USER_ALREADY_EXISTS"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    
    # Project errors
    PROJECT_NOT_FOUND = "PROJECT_NOT_FOUND"
    PROJECT_ALREADY_EXISTS = "PROJECT_ALREADY_EXISTS"
    INVALID_PROJECT_STATUS = "INVALID_PROJECT_STATUS"
    
    # File errors
    FILE_NOT_FOUND = "FILE_NOT_FOUND"
    FILE_TOO_LARGE = "FILE_TOO_LARGE"
    INVALID_FILE_TYPE = "INVALID_FILE_TYPE"
    
    # Blockchain errors
    BLOCKCHAIN_ERROR = "BLOCKCHAIN_ERROR"
    INSUFFICIENT_BALANCE = "INSUFFICIENT_BALANCE"
    TRANSACTION_FAILED = "TRANSACTION_FAILED"

class BaseException(Exception):
    """Base exception class"""
    
    def __init__(
        self,
        message: str,
        error_code: ErrorCode,
        details: Optional[Dict[str, Any]] = None,
        status_code: int = 500
    ):
        self.message = message
        self.error_code = error_code
        self.details = details or {}
        self.status_code = status_code
        super().__init__(message)
        
        # Log the exception
        logger.error(
            f"Exception: {error_code.value} - {message}",
            extra={"error_code": error_code.value, "details": details}
        )

class ValidationError(BaseException):
    """Validation error"""
    
    def __init__(
        self,
        message: str = "Validation failed",
        field_errors: Optional[List[Dict[str, str]]] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        self.field_errors = field_errors or []
        error_details = {"field_errors": self.field_errors}
        if details:
            error_details.update(details)
            
        super().__init__(
            message=message,
            error_code=ErrorCode.VALIDATION_ERROR,
            details=error_details,
            status_code=400
        )

class NotFoundError(BaseException):
    """Resource not found error"""
    
    def __init__(
        self,
        resource_type: str,
        resource_id: str,
        details: Optional[Dict[str, Any]] = None
    ):
        message = f"{resource_type} with ID {resource_id} not found"
        super().__init__(
            message=message,
            error_code=ErrorCode.NOT_FOUND,
            details=details,
            status_code=404
        )

class UnauthorizedError(BaseException):
    """Unauthorized access error"""
    
    def __init__(
        self,
        message: str = "Unauthorized access",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            error_code=ErrorCode.UNAUTHORIZED,
            details=details,
            status_code=401
        )

class ForbiddenError(BaseException):
    """Forbidden access error"""
    
    def __init__(
        self,
        message: str = "Access forbidden",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            error_code=ErrorCode.FORBIDDEN,
            details=details,
            status_code=403
        )
'''

    def _get_logging_setup(self) -> str:
        return '''"""
Logging configuration and setup
"""

import logging
import logging.config
import os
import sys
from typing import Dict, Any

def get_logging_config() -> Dict[str, Any]:
    """Get logging configuration"""
    
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            },
            "json": {
                "()": "packages.common.logging.formatters.JSONFormatter",
            },
        },
        "handlers": {
            "console": {
                "level": log_level,
                "class": "logging.StreamHandler",
                "formatter": "json" if os.getenv("LOG_FORMAT") == "json" else "standard",
                "stream": sys.stdout,
            },
            "file": {
                "level": log_level,
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "json",
                "filename": "logs/application.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
            },
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "sqlalchemy.engine": {
                "handlers": ["console"],
                "level": "WARNING",
                "propagate": False,
            },
        },
    }
    
    # Add file handler in production
    if os.getenv("ENVIRONMENT") == "production":
        config["loggers"][""]["handlers"].append("file")
    
    return config

def setup_logging():
    """Setup logging configuration"""
    
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    # Apply logging configuration
    logging.config.dictConfig(get_logging_config())
    
    # Log startup message
    logger = logging.getLogger(__name__)
    logger.info("Logging configured successfully")
'''

    def _get_logging_formatters(self) -> str:
        return '''"""
Custom logging formatters
"""

import json
import logging
import traceback
from datetime import datetime
from typing import Dict, Any

class JSONFormatter(logging.Formatter):
    """JSON log formatter"""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON"""
        
        log_data: Dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # Add process and thread info
        log_data["process"] = record.process
        log_data["thread"] = record.thread
        
        # Add extra fields
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
            
        if hasattr(record, "trace_id"):
            log_data["trace_id"] = record.trace_id
        
        # Add exception info
        if record.exc_info:
            log_data["exception"] = {
                "type": record.exc_info[0].__name__ if record.exc_info[0] else None,
                "message": str(record.exc_info[1]) if record.exc_info[1] else None,
                "traceback": traceback.format_exception(*record.exc_info),
            }
        
        # Add any extra attributes
        for key, value in record.__dict__.items():
            if key not in log_data and not key.startswith("_"):
                try:
                    json.dumps(value)  # Test if value is JSON serializable
                    log_data[key] = value
                except (TypeError, ValueError):
                    log_data[key] = str(value)
        
        return json.dumps(log_data, ensure_ascii=False)

class StructuredFormatter(logging.Formatter):
    """Structured text formatter for development"""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record with structure"""
        
        # Base format
        formatted = super().format(record)
        
        # Add extra context if available
        extras = []
        if hasattr(record, "user_id"):
            extras.append(f"user_id={record.user_id}")
        
        if hasattr(record, "request_id"):
            extras.append(f"request_id={record.request_id}")
        
        if extras:
            formatted += f" [{', '.join(extras)}]"
        
        return formatted
'''

    def _get_frontend_app_tsx(self) -> str:
        return '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

import { AuthProvider } from './context/AuthContext';
import HomePage from './pages/public/HomePage';
import DashboardPage from './pages/dashboard/DashboardPage';
import ProjectsPage from './pages/projects/ProjectsPage';
import RegistryPage from './pages/registry/RegistryPage';

const theme = createTheme({
  palette: {
    primary: {
      main: '#2e7d32', // Green theme for carbon/environmental focus
    },
    secondary: {
      main: '#1976d2',
    },
  },
});

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 3,
      staleTime: 5 * 60 * 1000, // 5 minutes
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <AuthProvider>
          <Router>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/dashboard" element={<DashboardPage />} />
              <Route path="/projects" element={<ProjectsPage />} />
              <Route path="/registry" element={<RegistryPage />} />
            </Routes>
          </Router>
        </AuthProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
'''

    def _get_api_client(self) -> str:
        return '''import axios, { AxiosInstance, AxiosResponse } from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: 10000,
    });

    // Request interceptor to add auth token
    this.client.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    // Response interceptor for error handling
    this.client.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response?.status === 401) {
          localStorage.removeItem('access_token');
          window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }

  // User endpoints
  async getProfile() {
    const response = await this.client.get('/api/v1/users/me');
    return response.data;
  }

  async updateProfile(data: any) {
    const response = await this.client.put('/api/v1/users/me', data);
    return response.data;
  }

  // Project endpoints
  async getProjects(params?: any) {
    const response = await this.client.get('/api/v1/projects', { params });
    return response.data;
  }

  async getProject(id: string) {
    const response = await this.client.get(`/api/v1/projects/${id}`);
    return response.data;
  }

  async createProject(data: any) {
    const response = await this.client.post('/api/v1/projects', data);
    return response.data;
  }

  async updateProject(id: string, data: any) {
    const response = await this.client.put(`/api/v1/projects/${id}`, data);
    return response.data;
  }

  async uploadDocument(projectId: string, file: File, documentType: string) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('document_type', documentType);

    const response = await this.client.post(
      `/api/v1/projects/${projectId}/documents`,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );
    return response.data;
  }

  // Authentication endpoints
  async login(email: string, password: string) {
    const response = await this.client.post('/api/v1/auth/login', {
      email,
      password,
    });
    return response.data;
  }

  async register(userData: any) {
    const response = await this.client.post('/api/v1/auth/register', userData);
    return response.data;
  }

  async refreshToken() {
    const response = await this.client.post('/api/v1/auth/refresh');
    return response.data;
  }
}

export default new ApiClient();
'''

    def _get_k8s_namespace(self) -> str:
        return '''apiVersion: v1
kind: Namespace
metadata:
  name: prism-carbon-registry
  labels:
    name: prism-carbon-registry
    environment: development
'''

    def _get_terraform_main(self) -> str:
        return '''terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# EKS Cluster
module "eks" {
  source = "./modules/eks"
  
  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version
  
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnets
  
  node_groups = var.node_groups
  
  tags = var.tags
}

# VPC
module "vpc" {
  source = "./modules/vpc"
  
  name = "${var.cluster_name}-vpc"
  cidr = var.vpc_cidr
  
  availability_zones = var.availability_zones
  
  tags = var.tags
}

# RDS Database
module "rds" {
  source = "./modules/rds"
  
  identifier = "${var.cluster_name}-postgres"
  engine     = "postgres"
  
  allocated_storage = var.db_allocated_storage
  instance_class    = var.db_instance_class
  
  db_name  = var.db_name
  username = var.db_username
  
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.database_subnets
  
  tags = var.tags
}

# ElastiCache Redis
module "redis" {
  source = "./modules/redis"
  
  cluster_id = "${var.cluster_name}-redis"
  
  node_type = var.redis_node_type
  
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets
  
  tags = var.tags
}
'''

    def _get_prometheus_config(self) -> str:
        return '''global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'api-gateway'
    static_configs:
      - targets: ['api-gateway:8000']
    metrics_path: /metrics
    scrape_interval: 5s

  - job_name: 'user-service'
    static_configs:
      - targets: ['user-service:8000']
    metrics_path: /metrics
    scrape_interval: 5s

  - job_name: 'project-service'
    static_configs:
      - targets: ['project-service:8000']
    metrics_path: /metrics
    scrape_interval: 5s

  - job_name: 'registry-service'
    static_configs:
      - targets: ['registry-service:8000']
    metrics_path: /metrics
    scrape_interval: 5s

  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres:5432']
    metrics_path: /metrics

  - job_name: 'redis'
    static_configs:
      - targets: ['redis:6379']
    metrics_path: /metrics
'''

    # Add the main execution and run function
    def run(self):
        """Run the structure generator"""
        try:
            self.create_structure()
        except Exception as e:
            print(f"❌ Error creating structure: {e}")
            sys.exit(1)

def main():
    """Main entry point"""
    project_name = sys.argv[1] if len(sys.argv) > 1 else "prism-carbon-registry"
    
    generator = StructureGenerator(project_name)
    generator.run()

if __name__ == "__main__":
    main()
