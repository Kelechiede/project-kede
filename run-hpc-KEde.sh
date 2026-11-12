#!/bin/bash
#SBATCH --job-name=KEde-WeeklyTracker
#SBATCH --output=weekly-tracker-%j.out
#SBATCH --error=weekly-tracker-%j.err
#SBATCH --time=00:02:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=256M

# Stop the script if a command fails.
set -e

# Move to the directory from which the job was submitted.
cd "$SLURM_SUBMIT_DIR"

# Load Python from the cluster's module system.
# The exact module name will be confirmed on the cluster.
module load python/3.11.5

# Activate the Python virtual environment created on the cluster.
source hpc-venv/bin/activate

# Run the weekly report program.
python Project-HPC-KEde.py
