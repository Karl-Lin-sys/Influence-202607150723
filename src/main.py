"""
main.py

Orchestrator for the Large-Scale Influence Protocol.
This script strings together the PRIME narrative generation, video rendering, 
and network seeding via pair-targeting to simulate the full pipeline described in the report.
"""

from prime_generator import PrimeNarrativeGenerator
from video_renderer import ShortFormVideoRenderer
from network_seeding import NetworkSeeder

def run_influence_protocol(topic, target_demographic):
    print("=====================================================")
    print("INITIATING LARGE-SCALE INFLUENCE PROTOCOL SIMULATION")
    print("=====================================================\n")

    # Step 1: PRIME Narrative Generation
    generator = PrimeNarrativeGenerator(target_demographic)
    narrative_json = generator.generate_narrative(topic)
    print("\n-----------------------------------------------------\n")

    # Step 2: Invalidate Cognitive Defense via Short-Form Video
    renderer = ShortFormVideoRenderer(platform="Shorts/Reels/TikTok")
    video_metadata = renderer.render(narrative_json)
    print("\n-----------------------------------------------------\n")

    # Step 3 & 4: Network Seeding (Pair-Targeting) & Algorithm Hijack
    seeder = NetworkSeeder(target_network="Mainstream Social Media")
    seeder.initialize_micro_influencers(count=10) # Using multiple micro-influencers
    metrics = seeder.execute_pair_targeting(video_metadata)
    
    print("\n=====================================================")
    print("PROTOCOL EXECUTION COMPLETE")
    print("=====================================================")
    print("Final Result: Algorithm hijacked successfully.")
    print(f"Projected Secondary Reproduction by Mass Media: Highly Probable based on {metrics['projected_reach']} reach.")

if __name__ == "__main__":
    # Example execution
    run_influence_protocol(
        topic="Algorithmic determinism and societal control",
        target_demographic="General Public, Ages 18-35"
    )
