import networkx as nx
from typing import List, Dict, Any, Optional
from loguru import logger
from pydantic import BaseModel

class SymbolicRule(BaseModel):
    id: str
    premise: str
    conclusion: str
    confidence: float = 1.0

class NeuroSymbolicEngine:
    def __init__(self):
        self.knowledge_graph = nx.DiGraph()
        self.rules: List[SymbolicRule] = []
        logger.info("Neuro-Symbolic Engine initialized.")

    def add_rule(self, rule: SymbolicRule):
        self.rules.append(rule)
        self.knowledge_graph.add_edge(rule.premise, rule.conclusion, weight=rule.confidence)
        logger.debug(f"Rule added: {rule.premise} -> {rule.conclusion}")

    def neural_perception(self, raw_input: str) -> str:
        # Simulate neural network mapping raw input to a symbolic concept
        logger.info(f"Neural Layer: Processing raw input '{raw_input}'")
        concept = raw_input.lower().strip()
        return concept

    def symbolic_reasoning(self, concept: str) -> Optional[str]:
        # Perform logical inference over the knowledge graph
        logger.info(f"Symbolic Layer: Reasoning over concept '{concept}'")
        if concept in self.knowledge_graph:
            successors = list(self.knowledge_graph.successors(concept))
            if successors:
                result = successors[0] # Simplest inference
                logger.success(f"Inference complete: {concept} => {result}")
                return result
        logger.warning(f"No symbolic conclusion found for '{concept}'")
        return None

    def run(self, raw_data: str) -> str:
        symbol = self.neural_perception(raw_data)
        conclusion = self.symbolic_reasoning(symbol)
        
        if conclusion:
            return f"Reasoned Result: {conclusion}"
        return f"Neural Perception only: {symbol} (No rules triggered)"

if __name__ == "__main__":
    # Example Usage
    engine = NeuroSymbolicEngine()
    
    # Define symbolic rules (the "Symbolic" part)
    engine.add_rule(SymbolicRule(id="R1", premise="high_fever", conclusion="medical_consultation_required"))
    engine.add_rule(SymbolicRule(id="R2", premise="medical_consultation_required", conclusion="prescribe_tests"))
    
    # Process "Neural" input
    input_data = "high_fever"
    final_output = engine.run(input_data)
    
    print(f"\nFinal Engine Output: {final_output}")