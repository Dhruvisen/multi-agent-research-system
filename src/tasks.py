from crewai import Task
import yaml
import os

class ResearchTasks:
    def __init__(self):
        # Load task configs
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'tasks.yaml')
        with open(config_path, 'r') as f:
            self.tasks_config = yaml.safe_load(f)

    def research_task(self, agent, topic: str) -> Task:
        config = self.tasks_config['research_task']
        return Task(
            description=config['description'].format(topic=topic),
            expected_output=config['expected_output'],
            agent=agent
        )

    def analysis_task(self, agent, topic: str) -> Task:
        config = self.tasks_config['analysis_task']
        return Task(
            description=config['description'].format(topic=topic),
            expected_output=config['expected_output'],
            agent=agent,
            human_input=True # HITL: Review research results before analysis
        )

    def writing_task(self, agent, topic: str) -> Task:
        config = self.tasks_config['writing_task']
        return Task(
            description=config['description'].format(topic=topic),
            expected_output=config['expected_output'],
            agent=agent,
            human_input=True # HITL: Final review before report completion
        )
