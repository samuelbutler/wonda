# wonda
AutoGPT prompt template for file based instructions and advice

The goals and role of the AI as set in `ai_settings.yaml` should likely stay the same for all AI's regardless of their task. The goal of wonda is to create a general purpose AI that can be given instructions and advice through files within its workspace. This will allow you to control the AI's instructions by editing `instructions.txt` as well as give the AI advice while it is running by writing in `advice.txt`. Although if you write in 'advice.txt', you will likely need to tell the AI in-between commands to go read the file as it won't know the contents have changed. 

You should write your instructions for the AI in `instructions.txt`. It helps to be explicit and to break the task down into its subtasks if possible. This allows the AI to start with a high level overview of its strategy and will help it avoid getting stuck loop or doing nothing.

`ai_settings.yaml` should be in the root of your AutoGPT project.

The following files should be placed in the `auto_gpt_workspace` folder:

 - `instructions.txt`
 - `advice.txt`
 - `learnings.txt`
 - `strategy.txt`

I have included in the `/output/` folder the following files which AutoGPT using GPT-4 created using the prompts in this repository. I have included these as an example of what AutoGPT should be able to produce.
 - `sudoko_generator.py`
 - `sudoku_solver.py`
 - `sudoku_puzzle.json`
 - `strategy.txt` - this is just a planning document AutoGPT created
 - `file_logger.txt` - this is an automatically generated file anytime AutoGPT does file operations
