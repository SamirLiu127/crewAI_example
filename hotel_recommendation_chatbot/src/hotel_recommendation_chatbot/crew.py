from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from hotel_recommendation_chatbot.tools import (
    hotel_parameters_tools, 
    hotel_search_tools, 
    nearby_search_tools
)

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class HotelRecommendationChatbot():
	"""HotelRecommendationChatbot crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def user_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['user_analyst'],
			verbose=True,
			tools=hotel_parameters_tools
		)
	
	@agent
	def hotel_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['hotel_expert'],
			verbose=True,
			tools=hotel_search_tools
		)

	@agent
	def local_explorer(self) -> Agent:
		return Agent(
			config=self.agents_config['local_explorer'],
			verbose=True,
			tools=nearby_search_tools
		)

	@agent
	def travel_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['travel_advisor'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def initial_consultation_task(self) -> Task:
		return Task(
			config=self.tasks_config['initial_consultation_task'],
		)
	
	@task
	def hotel_search_task(self) -> Task:
		return Task(
			config=self.tasks_config['hotel_search_task'],
		)
	
	@task
	def local_exploration_task(self) -> Task:
		return Task(
			config=self.tasks_config['local_exploration_task'],
		)
	
	@task
	def final_recommendation_task(self) -> Task:
		return Task(
			config=self.tasks_config['final_recommendation_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the HotelRecommendationChatbot crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
