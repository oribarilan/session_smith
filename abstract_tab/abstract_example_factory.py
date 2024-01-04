import random
from dataclasses import dataclass


@dataclass
class Topic:
    title: str
    tech: str
    domain: str


class AbstractExampleFactory:
    topics = [
        Topic("Implementing Machine Learning in Web Development", "Machine Learning", "Web Development"),
        Topic("Advances in Natural Language Processing for Chatbots", "Natural Language Processing", "Chatbots"),
        Topic("Agile Methodologies in Modern Software Teams", "Agile Methodologies", "Software Development"),
        Topic("Exploring the Potential of Quantum Computing", "Quantum Computing", "Computer Science"),
        Topic("Data-Driven Decision Making in Product Management", "Data-Driven Decision Making", "Product Management"),
        Topic("The Role of AI in Enhancing Cybersecurity", "Artificial Intelligence", "Cybersecurity"),
        Topic("Blockchain Technology: Beyond Cryptocurrency", "Blockchain Technology", "Finance"),
        Topic("Leveraging Big Data for Personalized User Experiences", "Big Data", "User Experience"),
        Topic("Ethical Considerations in AI Deployment", "Artificial Intelligence", "Ethics"),
        Topic("Integrating IoT with Cloud Computing for Smart Solutions", "Internet of Things", "Cloud Computing"),
        Topic("Performance Optimization Techniques in High-Load Systems", "Performance Optimization", "Systems"),
        Topic("DevOps Best Practices for Continuous Integration", "DevOps", "Software Development"),
        Topic("Predictive Analytics in E-commerce", "Predictive Analytics", "E-commerce"),
        Topic("User Experience Design: A Data-Driven Approach", "User Experience Design", "Data-Driven Decision Making"),
        Topic("Augmented Reality in Educational Technology", "Augmented Reality", "Education"),
        Topic("Building Scalable Microservices Architecture", "Microservices", "Software Architecture"),
        Topic("The Future of Mobile App Development with AI", "Artificial Intelligence", "Mobile App Development"),
        Topic("Effective Strategies for Technical Project Management", "Technical Project Management", "Project Management"),
        Topic("Data Privacy Laws and Their Impact on Big Data", "Data Privacy", "Big Data"),
        Topic("Serverless Architectures: Pros and Cons", "Serverless Architectures", "Software Architecture"),
        Topic("Sustainable Computing and Green IT Initiatives", "Sustainable Computing", "Green IT"),
        Topic("Containerization with Docker and Kubernetes", "Containerization", "Software Architecture"),
        Topic("The Impact of 5G on Internet of Things (IoT)", "5G", "Internet of Things"),
        Topic("Reinforcement Learning in Autonomous Vehicles", "Reinforcement Learning", "Autonomous Vehicles"),
        Topic("Strategies for Managing Technical Debt", "Technical Debt", "Software Development"),
        Topic("Cross-Platform Development with React Native", "React Native", "Mobile App Development"),
        Topic("Enhancing Database Performance with NewSQL", "NewSQL", "Databases"),
        Topic("Machine Learning in Financial Fraud Detection", "Machine Learning", "Finance"),
        Topic("Challenges and Solutions in Cloud Security", "Cloud Security", "Cybersecurity"),
        Topic("Building Interactive Data Visualizations", "Data Visualizations", "Data Science"),
        Topic("Voice Recognition Technologies in Smart Homes", "Voice Recognition", "Smart Homes"),
        Topic("API Design and Management Best Practices", "API Design", "Software Architecture"),
        Topic("Robotic Process Automation in Business Processes", "Robotic Process Automation", "Business Processes"),
        Topic("Graph Databases and Their Applications", "Graph Databases", "Databases"),
        Topic("Low-Code Development Platforms for Rapid Prototyping", "Low-Code Development Platforms", "Software Development"),
        Topic("Adaptive Learning Systems in Education", "Adaptive Learning Systems", "Education"),
        Topic("Real-Time Analytics and Stream Processing", "Real-Time Analytics", "Data Science"),
        Topic("Edge Computing in Industrial IoT", "Edge Computing", "Internet of Things"),
        Topic("Deep Learning for Medical Image Analysis", "Deep Learning", "Medical Image Analysis"),
        Topic("Managing High-Performance Computing Clusters", "High-Performance Computing", "Systems"),
        Topic("The Evolution of Software Testing Automation", "Software Testing Automation", "Software Development"),
        Topic("Collaborative Tools for Remote Development Teams", "Collaborative Tools", "Software Development"),
        Topic("Smart City Technologies and Urban Planning", "Smart City Technologies", "Urban Planning"),
        Topic("Fintech Innovations: Blockchain and Beyond", "Blockchain Technology", "Fintech"),
        Topic("Genetic Algorithms in Optimization Problems", "Genetic Algorithms", "Optimization"),
        Topic("Emotion Recognition Using AI", "Emotion Recognition", "Artificial Intelligence"),
        Topic("Wearable Technology in Healthcare Monitoring", "Wearable Technology", "Healthcare"),
        Topic("Next-Generation Wireless Networking", "Wireless Networking", "Computer Networks"),
        Topic("Mixed Reality in Gaming and Entertainment", "Mixed Reality", "Gaming"),
        Topic("Quantitative Models for Risk Management", "Quantitative Models", "Risk Management"),
    ]

    def _generate_session_description(self, topic: Topic) -> str:
        base_sentences = [
            f"This session provides an in-depth exploration of {topic.title}, highlighting its key concepts, tools, and real-world applications.",
            f"Attendees will learn about the latest advancements in {topic.tech} and how they can be applied to solve complex problems in {topic.domain}.",
            f"The presenter will share personal experiences from the {topic.domain} industry, describing challenges faced while working with {topic.tech}, offering insights into practical solutions and best practices.",
            f"Interactive demonstrations will showcase the power and versatility of {topic.tech}, encouraging participants to consider how they might integrate these technologies into their own work.",
            f"Discussion will also cover the future trajectory of {topic.tech}, considering emerging trends, potential impacts, and ethical considerations, and how it can be applied outside {topic.domain}."
        ]
        return " ".join(random.sample(base_sentences, random.randint(3, 5)))

    def generate(self):
        topic = random.choice(self.topics)
        length = random.choice(range(5, 61, 5))
        description = self._generate_session_description(topic)
        return topic, length, description
