# Multi-Agent Sales Orchestrator

A multi-agent AI workflow that generates, evaluates, and sends cold sales emails using locally hosted LLMs through Ollama and email delivery through SendGrid.

## Overview

This project demonstrates how multiple AI agents can collaborate to solve a business task.

Instead of relying on a single LLM response, the system creates multiple email drafts using specialized agents, evaluates them through a manager agent, selects the strongest draft, and automatically sends the chosen email using SendGrid.

The project was built to explore:

- Multi-agent architectures
- Agent orchestration
- Tool calling
- Local LLM inference with Ollama
- Automated email workflows

---

## Architecture

```text
                    Sales Manager Agent
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼

 Professional Agent   Engaging Agent    Concise Agent

         └───────────────────┼───────────────────┘
                             │
                             ▼

                    Evaluation Process
                             │
                             ▼

                      Winning Draft
                             │
                             ▼

                     SendGrid Tool
                             │
                             ▼

                      Email Delivery
```

---

## Demo Video

https://www.youtube.com/watch?v=W6qPk1-N2oQ

## Features

### Professional Sales Agent

Generates formal and professional cold sales emails.

### Engaging Sales Agent

Generates creative and engaging cold emails designed to increase response rates.

### Concise Sales Agent

Generates short and direct sales emails.

### Sales Manager Agent

Evaluates all generated drafts and selects the strongest email.

### SendGrid Integration

Automatically sends the selected email to the target recipient.

### Local LLM Execution

Uses Ollama with Llama 3.1 running locally.

No OpenAI API credits required.

---

## Tech Stack

- Python 3.12
- Ollama
- Llama 3.1
- SendGrid
- AsyncIO
- dotenv

---

## Project Structure

```text
app/
├── __init__.py
├── agents.py
├── config.py
├── email_service.py
├── main.py
├── sales_manager.py
├── simple_agent.py
├── tools.py
```

---

## Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/multi-agent-sales-orchestrator.git

cd multi-agent-sales-orchestrator
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Verify installation:

```bash
ollama list
```

Pull the model if required:

```bash
ollama pull llama3.1:8b-instruct-q4_K_M
```

---

## Configure Environment Variables

Create a `.env` file:

```env
SENDGRID_API_KEY=your_sendgrid_api_key
```

---

## Run Application

From the project root:

```bash
python -m app.main
```

---

## Sample Workflow

1. User requests a cold sales email.
2. Professional Agent creates draft #1.
3. Engaging Agent creates draft #2.
4. Concise Agent creates draft #3.
5. Sales Manager evaluates all drafts.
6. Best draft is selected.
7. SendGrid tool sends the winning email.

---

## Example Output

```text
=== Generating Professional Draft ===

=== Generating Engaging Draft ===

=== Generating Concise Draft ===

=== AI SELECTED EMAIL ===

Subject: Improve Customer Experience with AI

Dear CEO,

...

[TOOL] Sending email...

Status Code: 202
```

---

## Future Enhancements

- Lead research agent
- Company website analysis
- CRM integration
- LinkedIn profile enrichment
- RAG-powered prospect personalization
- Human approval workflow
- Email performance analytics
- Multi-channel outreach

---

## Key Learnings

This project explores important AI engineering concepts:

- Multi-agent systems
- Agent orchestration
- Tool invocation
- Prompt engineering
- Local LLM deployment
- Automated workflows
- API integrations

---

## License

MIT License
