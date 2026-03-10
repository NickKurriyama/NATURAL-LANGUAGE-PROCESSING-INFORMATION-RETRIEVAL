#!/bin/bash
#SBATCH --job-name=build-faiss
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=04:00:00

source /datastore/cndt_hangdv/miniconda3/etc/profile.d/conda.sh
conda activate ir-env

mkdir -p logs

cd /datastore/cndt_hangdv/music-project/information_retrieval
export PYTHONPATH=$(pwd)

echo "Start job: $SLURM_JOB_ID"
echo "Node: $SLURM_NODELIST"

python -m src.retriever.faiss_index