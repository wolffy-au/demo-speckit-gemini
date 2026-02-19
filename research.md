# Research Findings

## Python Version

**Decision**: Python 3.11
**Rationale**: Python 3.11 offers significant performance improvements and features beneficial for modern web frameworks like FastAPI and Streamlit. It's a stable and widely supported version.
**Alternatives considered**: Python 3.10 (also stable, but 3.11 offers better performance); Python 3.12+ (potentially less stable or fewer ecosystem supports for now).

## Primary Dependencies Versions

**Decision**: FastAPI 0.100.0, Pydantic v2.x, Streamlit 1.25.0
**Rationale**: These versions are current, stable, and offer good compatibility with each other. FastAPI 0.100.0 is a recent stable release. Pydantic v2 provides significant performance gains and improvements. Streamlit 1.25.0 is a recent stable release. (Specific patch versions to be determined during installation).
**Alternatives considered**: Older versions of FastAPI/Pydantic (less performant, fewer features); newer pre-release versions (potential instability).

## Testing Framework Version

**Decision**: pytest 7.4.x
**Rationale**: pytest 7.4.x is a stable and widely adopted version of the Python testing framework, offering excellent plugin support and features suitable for unit and integration testing of web applications.
**Alternatives considered**: unittest (built-in, but less feature-rich than pytest); nose2 (less common in modern Python projects).

## Target Platform / Deployment Environment

**Decision**: Docker container deployed to a cloud platform (e.g., AWS, GCP, Azure).
**Rationale**: Docker provides an isolated and consistent environment for both development and deployment, ensuring that the application runs the same way regardless of the underlying infrastructure. Cloud platforms offer scalability and managed services suitable for web applications.
**Alternatives considered**: Direct VM deployment (less scalable, more manual setup); Serverless functions (might be over-architected for this application scope).

## Scale/Scope Targets

**Decision**: Handle up to 1,000 concurrent users with typical mortgage calculation loads.
**Rationale**: This target represents a moderate user base, providing a reasonable starting point for a calculator application without over-engineering for extreme scale initially. Detailed profiling will inform scaling strategies later.
**Alternatives considered**: Very high scale (e.g., 100k concurrent users) - overkill for initial MVP; Very low scale (e.g., single-user desktop app) - does not align with web deployment.

<!--
  NOTE: The structure above is a basic example. For more complex findings,
  consider adding subsections for each research item.
-->
