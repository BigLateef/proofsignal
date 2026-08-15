from genlayer import *
import json

class ProofSignal(gl.Contract):
    records: DynArray[str]

    def __init__(self):
        self.records = DynArray[str]()

    @gl.public.write
    def verify_claim(self, claim: str, source_url: str):
        def evaluate():
            response = gl.nondet.web.request(source_url)
            text = response.body.decode("utf-8")[:12000]
            return gl.nondet.exec_prompt(
                "Return JSON with verdict VERIFIED, FALSE, or UNCLEAR, confidence 0-100, and evidence. Evaluate this claim against the source text. CLAIM: " + claim + " SOURCE: " + text,
                response_format="json",
            )
        result = gl.eq_principle.prompt_comparative(evaluate, "Compare validator JSON results and select the consensus result.")
        self.records.append(json.dumps({"claim": claim, "source_url": source_url, "result": result}, sort_keys=True))

    @gl.public.view
    def get_records(self):
        return [record for record in self.records]

