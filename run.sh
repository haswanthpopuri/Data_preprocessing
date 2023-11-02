#!/bin/bash

#SBATCH --job-name=crawler_job_test    # Job name

#SBATCH --mail-type=END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)

#SBATCH --mail-user=haswanthpopuri@ufl.edu     # Where to send mail	

#SBATCH --ntasks=4                    # Run on a single CPU

#SBATCH --mem=2gb                     # Job memory request

#SBATCH --time=12:00:00               # Time limit hrs:min:sec

#SBATCH --output=crawler_test_%j.log   # Standard output and error log

pwd; hostname; date

module load python

echo "Running plot script on a single CPU core"

python crawler.py

 

date