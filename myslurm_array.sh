#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 10:10:00
#SBATCH -p standard
#SBATCH -A phys_python
#SBATCH --job-name=MC_pi

#SBATCH --output=MC_pi_%A_%a.out
#SBATCH --error=MC_pi_%A_%a.error


python ./MC_pi.py 1000000000 ${SLURM_ARRAY_TASK_ID}

#This is a comment explaining how to run it...  
#sbatch --array=101-102 myslurm_array.sh
#sbatch --array=1001,1005 myslurm_array.sh
