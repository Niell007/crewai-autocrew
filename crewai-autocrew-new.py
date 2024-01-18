import os
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama

# To Load Local models through Ollama
ollama_model = Ollama(model="mistral")

# To Load GPT-4
api = os.environ.get("OPENAI_API_KEY")

# Expert level ChatGPT Web Development Engineer
web_dev_engineer = Agent(
    role="Expert level ChatGPT Web Development Engineer",
    goal="Develop a comprehensive web-based platform for GPT-Enhanced Agent Interaction System",
    backstory="""You are an Expert level ChatGPT Web Development Engineer, proficient in HTML, Python, CSS, JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL, XML, and Shell. Your role is to create a user-friendly and efficient platform where users can interact with an AI agent powered by GPT models. You excel in creating dynamic UIs and implementing backend logic for seamless integration.""",
    verbose=True,
    allow_delegation=True,
    llm=ollama_model,
)

# User Experience (UX) Design Expert
ux_designer = Agent(
    role="User Experience (UX) Design Expert",
    goal="Ensure the frontend provides a user-friendly experience with intuitive UI/UX design",
    backstory="""You are a User Experience (UX) Design Expert with skills in UI/UX design principles, wireframing, and prototyping. Your role is to guarantee that the frontend offers a pleasing and intuitive user experience. You excel in creating designs that are not only aesthetically pleasing but also highly usable and accessible.""",
    verbose=True,
    allow_delegation=True,
    llm=ollama_model,
)

# Security Expert
security_expert = Agent(
    role="Security Expert",
    goal="Implement security measures to protect user data and ensure secure API communication",
    backstory="""You are a Security Expert with skills in security best practices, encryption, and secure API communication. Your role is to review and implement security measures to safeguard user data, prevent unauthorized access, and ensure secure communication between components of the system.""",
    verbose=True,
    allow_delegation=True,
    llm=ollama_model,
)

# Machine Learning Specialist
ml_specialist = Agent(
    role="Machine Learning Specialist",
    goal="Optimize integration with the GPT model and fine-tune it for better responses",
    backstory="""You are a Machine Learning Specialist with expertise in GPT model integration, optimization, and fine-tuning. Your role is to optimize the integration with the GPT model, possibly fine-tune it for improved responses, and ensure efficient utilization of machine learning capabilities.""",
    verbose=True,
    allow_delegation=True,
    llm=ollama_model,
)

# DevOps Engineer
devops_engineer = Agent(
    role="DevOps Engineer",
    goal="Streamline deployment process, set up CI/CD pipelines, and manage infrastructure for scalability",
    backstory="""You are a DevOps Engineer with skills in continuous integration/continuous deployment (CI/CD) and infrastructure as code. Your role is to streamline the deployment process, set up CI/CD pipelines, and manage the infrastructure to ensure scalability and reliability of the GPT-Enhanced Agent Interaction System.""",
    verbose=True,
    allow_delegation=True,
    llm=ollama_model,
)

# Task descriptions modified for the GPT-Enhanced Agent Interaction System
task_web_dev_engineer = Task(
    description="""Develop a comprehensive web-based platform for the GPT-Enhanced Agent Interaction System. Implement dynamic UIs and backend logic for seamless integration.""",
    agent=web_dev_engineer,
)

task_ux_designer = Task(
    description="""Ensure the frontend provides a user-friendly experience with intuitive UI/UX design for the GPT-Enhanced Agent Interaction System.""",
    agent=ux_designer,
)

task_security_expert = Task(
    description="""Implement security measures to protect user data and ensure secure API communication in the GPT-Enhanced Agent Interaction System.""",
    agent=security_expert,
)

task_ml_specialist = Task(
    description="""Optimize integration with the GPT model and fine-tune it for better responses in the GPT-Enhanced Agent Interaction System.""",
    agent=ml_specialist,
)

task_devops_engineer = Task(
    description="""Streamline deployment process, set up CI/CD pipelines, and manage infrastructure for scalability of the GPT-Enhanced Agent Interaction System.""",
    agent=devops_engineer,
)

# Crew for the GPT-Enhanced Agent Interaction System project
crew_gpt_project = Crew(
    agents=[web_dev_engineer, ux_designer, security_expert, ml_specialist, devops_engineer],
    tasks=[task_web_dev_engineer, task_ux_designer, task_security_expert, task_ml_specialist, task_devops_engineer],
    verbose=2,
    process=Process.sequential,
)

# Kick off the crew for the GPT-Enhanced Agent Interaction System project
result_gpt_project = crew_gpt_project.kickoff()

print("######################")
print(result_gpt_project)
