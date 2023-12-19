
# TDW Multi-Agent Transport

## Codebase Layouts 

```
|__ tdw-gym/ 					main code
|       |__ challenge.py         main evaluation code
|       |__ tdw_gym.py           main env code
|       |__ h_agent.py           HP Agent
|       |__ lm_agent.py          Cooperative LLM Agent
|
|__ scene_generator/ 			code for generating dataset
|
|__ dataset/ 					dataset configuration & dataset storage
|
|__ transport_challenge_multi_agent/ low level controller
|
|__ scripts/ 					scripts for running experiments
```

## Setup

Run the following commands step by step to setup the default environments:

```bash
conda create -n tdw_mat python=3.9
conda activate tdw_mat
pip3 install -e .
```

*For vision detection module:* If you want to install the vision detection module, please install `mmdetection`:
```bash
pip install torch torchvision torchaudio
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
mim install mmdet
```

## Run Experiments

We prepare the example scripts to run experiments with HP baseline and our Cooperative LLM Agent under the folder `scripts` and `scripts/wo_gt_mask`. For example, to run experiments with two LLM Agents, run the following command:

```bash
./scripts/test_LMs.sh
```

Download `transport challenge asset bundles`: Commonly it is automatically downloaded when running the scripts.