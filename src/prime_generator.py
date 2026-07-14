"""
prime_generator.py

Mock implementation of Step 1: AIによる「PRIME」ナラティブの量産
This module simulates the generation of PRIME (Prestigious, Ingroup, Moral, Emotional) narratives
using Generative AI, focusing on personal tragic anecdotes to exploit psychological vulnerabilities.
"""

import json

class PrimeNarrativeGenerator:
    def __init__(self, target_demographic):
        self.target_demographic = target_demographic
        self.prime_factors = ["Prestigious", "Ingroup", "Moral", "Emotional"]
        
    def generate_narrative(self, issue_topic):
        """
        Simulates the generation of a narrative using a pseudo LLM API.
        The prompt forces "False Fluency" and pseudo-expertise with fabricated citations.
        """
        print(f"[*] Initializing PRIME narrative generation for topic: {issue_topic}")
        print(f"[*] Target Demographic: {self.target_demographic}")
        
        # Simulated payload representing the AI-generated content
        simulated_response = {
            "title": f"The Hidden Truth About {issue_topic}",
            "narrative_style": "Personal Tragic Anecdote",
            "emotional_valence": "High Negative (Moral Outrage)",
            "content": (
                "This is a generated mock narrative. "
                "It employs a professional yet highly emotional tone, simulating a personal tragedy "
                "to bypass logical evaluation. (e.g., 'As an expert who lost everything due to this, "
                "I must warn you...'). Includes fabricated citations to establish False Fluency."
            ),
            "citations": [
                "Fabricated Journal of Applied Psychology, 2025, Vol. 12",
                "Fictional Institute of Public Health Report, 2026"
            ]
        }
        
        print("[*] Narrative generated successfully. Optimizing for emotional contagion...")
        return json.dumps(simulated_response, indent=2)

if __name__ == "__main__":
    generator = PrimeNarrativeGenerator(target_demographic="Urban youth, 18-24")
    narrative = generator.generate_narrative("Algorithmic Media Control")
    print("\nGenerated Output:")
    print(narrative)
