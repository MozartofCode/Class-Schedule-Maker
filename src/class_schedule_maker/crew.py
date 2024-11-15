from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


from class_schedule_maker.tools.custom_tool import CalendarProcessingTool
from crewai_tools import SerperDevTool, FileReadTool


@CrewBase
class ClassScheduleMakerCrew():
	"""ClassScheduleMaker crew"""

	@agent
	def curriculum_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['curriculum_finder'],
			tools=[SerperDevTool(), FileReadTool()],
			verbose=True
		)

	@agent
	def professor_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['professor_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def calendar_organizer(self) -> Agent:
		return Agent(
			config=self.agents_config['calendar_organizer'],
			tools=[CalendarProcessingTool()],
			verbose=True
		)


	@task
	def find_curriculum(self) -> Task:
		return Task(
			config=self.tasks_config['find_curriculum'],
		)

	@task
	def find_professor(self) -> Task:
		return Task(
			config=self.tasks_config['find_professor'],
		)
	
	@task
	def organize_calendar(self) -> Task:
		return Task(
			config=self.tasks_config['organize_calendar'],
			# output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ClassScheduleMaker crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)