# Add RAG Integration

Integrate Vertex AI RAG Engine into an existing ADK agent to ground responses in authoritative data sources with automatic citation extraction.

## Task

You are tasked with adding RAG (Retrieval-Augmented Generation) capabilities to an agent or creating a new RAG-enabled agent from scratch.

### RAG Integration Components

A complete RAG setup includes:

```
RAG System Structure:
├── Corpus Creation
│   └── Create Vertex AI RAG corpus with descriptive name
├── Document Ingestion
│   ├── Upload documents to GCS (if not already there)
│   └── Import GCS documents to corpus with chunking strategy
├── Agent Integration
│   ├── Create RAG retrieval tool with Tool.from_retrieval()
│   ├── Add tool to agent's tools list
│   └── Update system prompt with RAG constraints
└── Citation Extraction
    ├── Parse grounding_metadata from responses
    └── Format citations for user display
```

### Quality Standards (MANDATORY)

All RAG integrations MUST meet these standards:

1. **Corpus Management**:
   - Corpus has clear `display_name` and `description`
   - Embedding model explicitly configured (default: text-embedding-004)
   - Chunking strategy selected based on content type
   - Files successfully indexed before querying

2. **Citation Extraction (CRITICAL)**:
   - ALL RAG responses MUST extract `grounding_metadata`
   - Citations include source URI and text excerpt
   - Citations formatted for user display
   - Confidence scores included when available

3. **System Prompt Constraints**:
   - Prompt MUST include anti-hallucination instructions
   - Agent instructed to ONLY answer from retrieved documents
   - Agent instructed to cite sources by document name
   - Agent instructed to say "I don't have that information" if not in corpus

4. **Async Implementation**:
   - Corpus operations (create, import) are async
   - Error handling for rate limits and timeouts
   - Corpus state verification before querying

5. **Retrieval Configuration**:
   - `similarity_top_k` configured based on use case
   - `vector_distance_threshold` tuned for precision/recall balance
   - Multiple corpora supported if needed

### Implementation Steps

1. **Invoke rag-integration-agent**:
   - Agent gathers requirements (domain, document sources, query types)
   - Creates RAG corpus with appropriate configuration
   - Uploads documents to GCS (if not already there)
   - Imports documents with optimal chunking strategy
   - Waits for indexing completion
   - Creates RAG tool with Tool.from_retrieval()
   - Updates agent system prompt with RAG constraints
   - Implements citation extraction logic
   - Tests with sample queries

2. **Generate/Update Files**:
   - Update `agent.py` to include RAG tool
   - Update system prompt with anti-hallucination constraints
   - Add `rag_utils.py` with citation extraction functions
   - Update `README.md` with RAG setup and usage
   - Add corpus management scripts (optional)

3. **Quality Checks**:
   - Verify corpus created successfully
   - Verify documents indexed (check corpus status)
   - Verify RAG tool uses `Tool.from_retrieval()` pattern
   - Verify system prompt includes RAG constraints
   - Test citation extraction with sample queries
   - Verify agent doesn't answer without corpus data

### Chunking Strategy Selection

**Choose based on content type:**

| Content Type | Chunk Size | Overlap | Rationale |
|--------------|------------|---------|-----------|
| Technical documentation | 512 tokens | 100 tokens | Precise, self-contained sections |
| General content (default) | 1024 tokens | 200 tokens | Balanced context and precision |
| Long-form (books, articles) | 1536 tokens | 300 tokens | Preserves narrative flow |
| FAQ / Q&A pairs | 256 tokens | 0 tokens | Each pair is self-contained |

### Retrieval Parameter Tuning

**Precision vs Recall:**

| Use Case | top_k | distance_threshold | Effect |
|----------|-------|-------------------|--------|
| Specific factual queries | 5 | 0.2 | High precision, strict relevance |
| Balanced (recommended) | 10 | 0.3 | Good balance |
| Exploratory/broad queries | 20 | 0.5 | High recall, more coverage |

### System Prompt Template for RAG

```xml
<role>
You are a {domain} assistant that answers questions using our
authoritative knowledge base via RAG (Retrieval-Augmented Generation).
</role>

<instructions>
## Answer Process

### Step 1: Retrieval
For every factual question:
1. Use the RAG retrieval tool to search knowledge base
2. Review retrieved document chunks
3. Identify relevant information

### Step 2: Response Generation
1. ONLY use information from retrieved documents
2. Synthesize information clearly
3. Include source citations

### Step 3: Source Attribution
Format response with:
1. Direct answer to question
2. Supporting details from documents
3. **Sources:** section with citations
</instructions>

<tools>
**RAG Retrieval Tool**
- Searches knowledge base for relevant document chunks
- Returns text with source references
- Use for EVERY factual question

When to use: Any query requiring factual information from our knowledge base
When NOT to use: Greetings, clarifications, procedural questions about the system itself
</tools>

<constraints>
## Must Do
- ALWAYS use RAG retrieval for factual questions
- ALWAYS cite sources (document names and excerpts)
- ALWAYS stay within retrieved document content

## Must Never Do
- NEVER make up information not in retrieved documents
- NEVER answer factual questions without using RAG tool
- NEVER claim certainty if documents are ambiguous or conflicting

## When Information Not Found
If RAG retrieval returns no relevant documents:
"I don't have that information in my knowledge base. The documents I have
access to cover {domain_scope}. Your question about {topic} is outside
that scope."
</constraints>

<examples>
## Example 1: Information Found
<user_input>
What is our refund policy?
</user_input>

<assistant_response>
Our refund policy allows returns within 30 days of purchase for a full
refund, provided the item is unused and in original packaging. After 30
days, we offer store credit for up to 60 days.

Special conditions:
- Sale items: Exchange only, no refunds
- Custom orders: Non-refundable
- Damaged items: Full refund regardless of time period

**Sources:**
[1] Customer_Service_Policy_2025.pdf: "Standard return window is 30 days..."
[2] Refund_Guidelines.pdf: "Sale items are eligible for exchange only..."
</assistant_response>

## Example 2: Information Not Found
<user_input>
What is the CEO's favorite restaurant?
</user_input>

<assistant_response>
I don't have that information in my knowledge base. The documents I have
access to cover company policies, procedures, and benefits. Personal
preferences of executives are not included in these materials.
</assistant_response>
</examples>
```

### Example Usage

```bash
# User wants to add RAG to existing agent
/add-rag

Agent: customer_support_agent
Documents location: gs://my-company-docs/support-kb/
Document types: FAQ PDFs, policy documents, troubleshooting guides
Expected queries: Customer questions about policies, troubleshooting, returns

# rag-integration-agent sets up complete RAG pipeline
```

**Result:**
```
✅ RAG Integration Complete

Corpus Details:
- Name: Customer Support Knowledge Base
- ID: projects/my-proj/locations/us-central1/ragCorpora/12345
- Documents: 47 files indexed
- Chunk strategy: 1024 tokens, 200 overlap

Agent Updates:
- Added RAG retrieval tool
- Updated system prompt with anti-hallucination constraints
- Implemented citation extraction
- Added query_with_citations() function

Test Results:
Query: "What is the return policy?"
Response: [detailed answer with 2 citations]
Citations: 2 sources found
- Customer_Service_Guide.pdf
- Return_Policy_2025.pdf

Agent ready for production use with grounded, cited responses.
```

### Citation Extraction Template

```python
async def query_with_citations(
    agent: types.LlmAgent,
    query: str
) -> dict[str, any]:
    """
    Query RAG agent and extract citations.

    Returns:
        {
            "response": "text response",
            "citations": [
                {"uri": "gs://...", "text": "excerpt", "confidence": 0.95}
            ]
        }
    """
    client = genai.Client(vertexai=True)
    chat = client.aio.chats.create(agent=agent)
    response = await chat.send_message(query)

    # Extract grounding metadata
    citations = []
    if hasattr(response, 'candidates') and response.candidates:
        candidate = response.candidates[0]
        if hasattr(candidate, 'grounding_metadata'):
            metadata = candidate.grounding_metadata
            if hasattr(metadata, 'grounding_supports'):
                for support in metadata.grounding_supports:
                    citations.append({
                        "uri": getattr(support.segment, 'uri', 'Unknown'),
                        "text": getattr(support.segment, 'text', '')[:200],
                        "confidence": getattr(support, 'confidence_score', None)
                    })

    return {"response": response.text, "citations": citations}
```

### Validation Checklist

After RAG integration, verify:
- ✅ Corpus created with clear name and description
- ✅ Documents successfully uploaded and indexed
- ✅ RAG tool uses `Tool.from_retrieval()` pattern
- ✅ System prompt includes anti-hallucination constraints
- ✅ `grounding_metadata` extraction implemented
- ✅ Citations formatted for display
- ✅ Agent refuses to answer without retrieved docs
- ✅ Test queries return citations
- ✅ Source URIs are valid and accessible

### Troubleshooting

**Problem: No citations extracted**
```python
# Check if grounding_metadata exists
print(hasattr(response.candidates[0], 'grounding_metadata'))

# Verify RAG tool is being called
# (Check agent logs or response metadata)
```

**Problem: Irrelevant retrievals**
```python
# Increase strictness
rag_tool = types.Tool.from_retrieval(
    retrieval=types.VertexRagStore(
        rag_resources=[types.RagResource(rag_corpus=corpus)],
        similarity_top_k=5,  # Reduce from 10
        vector_distance_threshold=0.2  # Stricter (was 0.3)
    )
)
```

**Problem: Missing relevant documents**
```python
# Increase recall
rag_tool = types.Tool.from_retrieval(
    retrieval=types.VertexRagStore(
        rag_resources=[types.RagResource(rag_corpus=corpus)],
        similarity_top_k=20,  # Increase from 10
        vector_distance_threshold=0.5  # More lenient (was 0.3)
    )
)
```

## Prompt

I need to add RAG capabilities to an agent (or create a new RAG-enabled agent).

**Requirements:**
- Domain: {knowledge_domain}
- Documents location: {gcs_bucket_or_local_paths}
- Document types: {pdf_txt_html_etc}
- Expected queries: {query_examples}
- Precision vs recall preference: {strict_or_comprehensive}

Please use the rag-integration-agent to set up a complete RAG pipeline with corpus creation, document ingestion, agent integration, and citation extraction following all Vibekit RAG standards.
