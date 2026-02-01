# agentient-rag-engine

Production-grade Retrieval-Augmented Generation (RAG) pipeline plugin for Google Cloud Vertex AI RAG Engine with asymmetric embeddings, intelligent chunking, and mandatory citation attribution.

**Confidence**: 99% | **Category**: Backend | **Version**: 1.0.0

## Key Features

- **Asymmetric Embedding Strategy**: RETRIEVAL_DOCUMENT for ingestion, RETRIEVAL_QUERY for queries
- **Concurrent Online Embeddings**: Bypasses batch API limitation, ensures correct task_type
- **Intelligent Chunking**: Fixed, semantic, sentence-boundary, markdown-aware strategies
- **Mandatory Citation Attribution**: Source URI, chunk ID, confidence score, character offsets
- **Performance Optimization**: Re-ranking, query expansion, semantic caching

## Critical Architecture Patterns

### 1. Never Use Batch Embeddings for Documents
Batch API defaults to RETRIEVAL_QUERY → semantic mismatch → poor retrieval.
**Solution**: Concurrent online embeddings with explicit RETRIEVAL_DOCUMENT.

### 2. Asymmetric task_type is Non-Negotiable
Documents and queries must use different task_types for optimal semantic search.

### 3. Chunk Strategy Matches Document Structure
| Type | Strategy |
|------|----------|
| Prose | Fixed-size (512-1000 tokens) |
| Legal docs | Semantic (paragraphs) |
| Q&A | Sentence-boundary |
| Tech docs | Markdown-aware |

## Components

- **Agent**: rag-engineer-agent
- **Commands**: /create-corpus, /ingest-documents, /query-rag, /optimize-retrieval
- **Skills** (6): corpus-lifecycle, intelligent-ingestion, embedding-strategy, advanced-query, performance-tuning, pydantic-schema

## Dependencies

**Required**: agentient-python-core, agentient-devops-gcp
**Optional**: agentient-adk-agents

---

**Generated with Claude Code** | Version 1.0.0
