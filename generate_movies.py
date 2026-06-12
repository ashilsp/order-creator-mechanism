#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.visualization import render_movie_s2, render_movie_s3

def main():
    print("🚀 Initializing Order Creator Mechanism Simulation Suite...")
    print("\n🎬 Processing: Movie S2 (Volumetric Capture Loop)...")
    render_movie_s2("movie_s2_sequestration.mp4")
    print("✅ Movie S2 successfully compiled.")
    
    print("\n🎬 Processing: Movie S3 (Vacuum Scaling Law Dilution)...")
    render_movie_s3("movie_s3_vacuum_dilution.mp4")
    print("✅ Movie S3 successfully compiled.")
    print("\n🎉 Complete. All supplementary simulation files have compiled cleanly.")

if __name__ == "__main__":
    main()
