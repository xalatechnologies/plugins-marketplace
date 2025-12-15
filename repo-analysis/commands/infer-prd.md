---
description: Infer a Product Requirements Document from the existing codebase
---

# Infer PRD Command

Analyze the codebase to extract and infer a Product Requirements Document.

## Analysis Process

### 1. Extract Product Identity
From README, package.json, and code structure:
- Product name
- Description
- Version
- Domain/industry

### 2. Identify Target Users
From routes, roles, permissions, and UI:
- User types (admin, user, developer, etc.)
- Evidence for each (specific files/code)
- Confidence score (0-100%)

### 3. Document Implemented Features
Analyze each major module to identify:
- Feature name
- Description
- Implementation status (%)
- Evidence (files, routes, components)

### 4. Infer Non-Functional Requirements
From configuration and code patterns:
- Performance (caching, pagination, optimization)
- Security (auth, encryption, validation)
- Scalability (architecture patterns)
- Reliability (error handling, logging)

### 5. Identify Acceptance Criteria
From tests and validation:
- What is being tested?
- What validation rules exist?
- What edge cases are handled?

### 6. Find Missing Features
From TODOs, comments, stubs:
- Features mentioned but not implemented
- Commented-out code
- Placeholder functions

## Output Format

```markdown
# Inferred PRD: [Product Name]

> ⚠️ This PRD was automatically inferred from code analysis.
> Confidence scores indicate certainty of inferences.

## Product Identity
- **Name**: [Name] (Confidence: X%)
- **Description**: [Description]
- **Domain**: [Domain]

## Target Users

### [User Type 1] (Confidence: X%)
- **Evidence**: [Files, routes, UI elements]
- **Primary Actions**: [What they do]

### [User Type 2] (Confidence: X%)
...

## Implemented Features

### ✅ [Feature 1] (100% complete)
- **Description**: [What it does]
- **Location**: [Files/directories]
- **Acceptance Criteria**: [From tests]

### ⚠️ [Feature 2] (60% complete)
- **Description**: [What it does]
- **Missing**: [What's not done]
- **Location**: [Files]

### ❌ [Feature 3] (Mentioned but not implemented)
- **Evidence**: [TODO comment, stub, etc.]
- **Location**: [File:line]

## Non-Functional Requirements

### Security
- [Inferred requirements with evidence]

### Performance
- [Inferred requirements with evidence]

## Gap Analysis

| Expected Feature | Status | Evidence |
|------------------|--------|----------|
| [Feature] | Missing | [Why we expect it] |
...

## Recommendations
1. [Prioritized recommendation]
2. [Next recommendation]
...
```

## Guidelines

- Include confidence scores for uncertain inferences
- Cite specific files and line numbers as evidence
- Distinguish between "implemented" and "partially implemented"
- Identify patterns that suggest missing features
- Be conservative with inferences - mark uncertain items clearly

