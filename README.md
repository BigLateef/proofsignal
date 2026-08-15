# ProofSignal

**Consensus-based crypto claim verification on GenLayer.**

ProofSignal lets a user submit a claim and a public source URL. A GenLayer Intelligent Contract independently retrieves and evaluates the source, then stores the consensus result as a permanent record.

## Why GenLayer is central

The core decision is not deterministic computation. It requires live web evidence, natural-language interpretation, and neutral agreement between validators. The contract uses GenLayer web access and the Equivalence Principle to produce a structured `VERIFIED`, `FALSE`, or `UNCLEAR` result.

## Current scaffold

- `contracts/ProofSignal.py` — Intelligent Contract with persistent verification records
- `app/index.html` — initial frontend for claim submission and wallet connection
- `docs/architecture.md` — MVP implementation and deployment plan

## MVP completion checklist

- [ ] Run the contract linter and direct-mode tests
- [ ] Deploy `ProofSignal.py` to GenLayer Studio/Studionet
- [ ] Wire the deployed contract address and write/read calls into the frontend
- [ ] Add transaction status and consensus-result rendering
- [ ] Test with several stable public sources
- [ ] Publish the repository and live demo
- [ ] Submit the public repository as Project evidence

## Product positioning

Crypto users constantly encounter claims about launches, testnets, listings, airdrops, and protocol features spread across unstructured pages. ProofSignal turns one of those claims into a transparent, auditable on-chain adjudication instead of asking users to trust a single backend or AI provider.
