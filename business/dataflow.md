# Dataflow Architecture for System Sculptor

## External Data Sources
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Code Repos    │    │   Dev Tools     │    │   Metrics API   │
│   (GitHub,     │    │   (CI/CD,      │    │   (Prometheus,  │
│   GitLab)       │    │   SonarQube)    │    │   Grafana)      │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                         ┌───────▼───────┐
                         │  External     │
                         │  Data Feeds   │
                         └───────────────┘
```

## Ingestion Layer
- GitHub/GitLab API connector (OAuth2)
- CI/CD pipeline event listener (Webhook handler)
- SonarQube metrics collector
- Prometheus/Grafana metric scraper
- File upload handler (for manual code analysis)
- Authentication gateway (JWT/OAuth2)

## Processing/Transform Layer
- Code parser (AST-based analysis)
- Dependency graph builder
- Architecture pattern matcher
- Risk scoring engine (severity classification)
- Metric aggregation processor
- Security vulnerability scanner
- Performance impact analyzer

## Storage Tier
- PostgreSQL (metadata store - 100GB max)
- Redis (session/cache - 50GB max)
- Vector DB (pgvector - 200GB max)
- S3 (artifact storage - 1TB max)
- Elasticsearch (search index - 100GB max)

## Query/Serving Layer
- GraphQL API gateway
- RESTful microservices (3 services)
- Real-time WebSocket endpoint
- Batch processing scheduler
- Caching layer (Redis)
- Rate limiting middleware
- Monitoring dashboard (Prometheus/Grafana)

## Egress to User
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Console   │    │   CLI Tool      │    │   API Endpoints │
│   (React App)   │    │   (Python SDK)  │    │   (REST/GraphQL)│
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                         ┌───────▼───────┐
                         │   User        │
                         │   Interface   │
                         └───────────────┘
```

## Auth Boundaries
- **Tier 1**: OAuth2/JWT authentication for all external APIs
- **Tier 2**: Role-based access control (RBAC) for user permissions
- **Tier 3**: Service-to-service authentication (mTLS)
- **Tier 4**: Data encryption at rest (AES-256) and in transit (TLS 1.3)
- **Tier 5**: Audit logging with immutable records for compliance