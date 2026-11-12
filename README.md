# Weekly Task & Habit Tracker

## Project Description

This project is a Weekly Task & Habit Tracker developed using Python as part of the ACENET Microcredential in Practical Foundations for Data Analytics.

The program helps users organize their weekly activities and daily habits. Users can add tasks and habits, mark them as completed, remove activities they no longer need, and view progress reports.

The project also includes a High-Performance Computing (HPC) component that generates weekly reports from ten different datasets using the ACENET training cluster.

## Features

The tracker allows users to:

1. Add tasks for specific days of the week.
2. Add daily habits.
3. Mark tasks and habits as completed.
4. Remove tasks and habits.
5. View daily and weekly progress reports.
6. Use a menu to select different actions.

## How to Use the Tracker

1. Download or clone this GitHub repository.
2. Open `Project-parts1-2-3-KEde.ipynb` using Jupyter Notebook or JupyterLab.
3. Run the notebook cells in order.
4. Follow the instructions displayed by the program.
5. Use the main menu to add, complete, or remove tasks and habits.
6. Select the reporting option to view your progress.

The program runs in Python and uses a command-line-style menu for user interaction.

## HPC Component

The HPC part of the project uses the following files:

- `Project-HPC-KEde.py` — Python program for generating weekly reports.
- `dictionaries_1.txt` to `dictionaries_10.txt` — Input datasets.
- `run-hpc-KEde.sh` — Slurm batch script used to run the program on ACENET.

The HPC program uses Python 3.11.5 and the `asteval` library.

### Running the HPC Program on ACENET

After transferring the required files to the training cluster, load Python and activate a virtual environment with `asteval` installed.

Submit the Slurm job using:

```bash
sbatch run-hpc-KEde.sh
```

Check the job status using:

```bash
sacct -j JOB_ID --format=JobID,State,ExitCode,Elapsed,MaxRSS
```

Check resource efficiency using:

```bash
seff JOB_ID
```

Replace `JOB_ID` with the actual job number assigned by Slurm.

## HPC Results

My final optimized HPC job was Job 17.

- Status: COMPLETED
- Exit code: 0
- CPU allocation: 1 CPU
- Memory allocation: 256 MB
- Time limit: 2 minutes
- Actual execution time: 1 second
- Memory used: 16.46 MB
- CPU efficiency: 100%
- Memory efficiency: 6.43%
- Weekly reports generated: 10

The program completed successfully without errors.

## Technologies Used

- Python
- Jupyter Notebook
- Git and GitHub
- ACENET HPC training cluster
- Slurm workload manager
- Python virtual environments
- asteval library

## Author

Kelechukwu Innocent Ede

ACENET Microcredential in Practical Foundations for Data Analytics

November 2026