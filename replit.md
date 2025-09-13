# Overview

The FUNETEC System is a Django-based project and contract management application developed for the Fundação de Apoio à Pesquisa e ao Desenvolvimento Tecnológico da Paraíba (FUNETEC-PB). The system manages the complete lifecycle of projects, from initial requests to contract execution and payment processing, with comprehensive user authentication and role-based access control.

## Current Status (September 2025)

✅ **CORE BUSINESS RULES IMPLEMENTED:**
- **RF-02, RF-21**: Prestador (Service Provider) management with PF/PJ differentiation and automatic tax calculations
- **RF-05, RF-06, RF-07**: Cost control system with budget vs actual tracking and traffic light indicators  
- **RF-08, RF-09, RF-10, RF-11**: Payment calculation rules supporting single payment or 2-installment options
- **Database**: All migrations applied successfully, proper constraints and relationships established
- **Forms**: Bootstrap-styled forms with comprehensive validation for Prestador and Contrato models

✅ **SYSTEM OPERATIONAL**: Django server running, database functional, ready for development and testing.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Backend Architecture

The system follows Django's modular architecture with a well-organized app structure:

- **Core App**: Provides base models, mixins, middleware, and common utilities
- **Accounts App**: Custom user authentication with extended profiles and role-based permissions
- **Projects App**: Manages projects, requisitions, orders, and cost tracking with signal-based automatic calculations
- **Contracts App**: Handles contract creation, payment installments, and contractor management
- **Dashboard App**: Analytics and metrics visualization for different user roles
- **Payments App**: Payment gateway integration (MercadoPago) with webhook handling
- **Reports App**: PDF and Excel report generation system
- **Clients App**: Customer relationship management

## Database Design

The system uses Django's ORM with SQLite for development (PostgreSQL ready for production). Key models include:

- **User**: Custom user model with roles (admin, ti, fiscal, financeiro, analista, cliente)
- **Project-Request-Order hierarchy**: Three-tier project management structure
- **Contract-Item relationship**: Contract management with installment tracking
- **Audit trails**: Automatic tracking of changes and user activities

## Authentication & Authorization

- Custom User model extending AbstractUser with department and role fields
- Role-based permissions system with granular access control
- External client support with is_cliente_externo flag
- Session-based authentication with remember-me functionality

## Frontend Architecture

- Bootstrap 5 for responsive UI components
- Django Crispy Forms for form rendering and validation
- Chart.js for dashboard analytics and data visualization
- Custom CSS with CSS variables for theming and consistency
- Progressive enhancement with vanilla JavaScript

## Design Patterns Implementation

- **Template Method**: Used in authentication views for different user types
- **Strategy Pattern**: Implemented for user role-based redirects and permissions
- **Observer Pattern**: Django signals for automatic cost calculations
- **Decorator Pattern**: UserProfile extends User functionality
- **Factory Pattern**: Form creation based on user roles and permissions

# External Dependencies

## Third-Party Services
- **MercadoPago SDK**: Payment gateway integration for contract payments
- **Django REST Framework**: API endpoints for data access and integration

## Key Python Packages
- **Django 4.2.7**: Web framework foundation
- **Crispy Forms**: Enhanced form rendering with Bootstrap 5 integration
- **Django Extensions**: Development utilities and enhanced management commands
- **ReportLab**: PDF generation for reports and contracts
- **OpenPyXL**: Excel file generation and data export
- **Pillow**: Image processing for user avatars and file uploads
- **Celery & Redis**: Asynchronous task processing (configured but not yet implemented)
- **Gunicorn**: Production WSGI server

## Development Tools
- **Django Debug Toolbar**: Development debugging (implied)
- **Python Decouple**: Environment variable management for configuration
- **Django Environ**: Additional environment configuration support

## Database
- **SQLite**: Development database (current)
- **PostgreSQL**: Production database (psycopg2-binary included for future migration)

## Static Assets
- **Bootstrap 5.3.0**: CSS framework via CDN
- **Font Awesome 6.4.0**: Icon library via CDN
- **Chart.js**: Data visualization library via CDN