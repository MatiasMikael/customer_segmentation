import subprocess

# Define the scripts to run
scripts = [
    "1_scripts/load_and_convert.py",
    "1_scripts/customer_segmentation.py",
    "1_scripts/rfm_clustering.py",
    "1_scripts/cluster_visualization.py"
]

# Execute each script sequentially
for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run(["python", script], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"{script} completed successfully!\n")
    else:
        print(f"Error while running {script}:\n{result.stderr}\n")
        print("Stopping pipeline due to an error.")
        break

print("All scripts executed.")