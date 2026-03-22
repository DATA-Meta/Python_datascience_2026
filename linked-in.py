#!/usr/bin/env python3
"""
LinkedIn Content Organizer for ML Students
Helps organize daily learning into LinkedIn-ready posts
Based on COM7022: Machine Learning at Arden University

Author: Your Name
Date: 2025
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


class LinkedInContentOrganizer:
    """Organizes daily ML learning into LinkedIn posts"""
    
    # Post templates based on course content
    TEMPLATES = {
        "ml_concept": """Day {day} of ML at Arden University:

Today I learned about {topic}.

What it is: {explanation}

Why it matters: {application}

My take: {personal_insight}

What ML concept are you learning? Let's connect!

#MachineLearning #DataScience #LearningInPublic #ArdenUniversity #StudentLife""",
        
        "code_tip": """Python Tip from today's ML class:

{topic}

Problem: {problem}
Solution: {solution}

Why it works: {explanation}

Save this for later! 📌

#Python #DataScience #CodingTips #MachineLearning""",
        
        "weekly_update": """Week {week} update: {topic}

What I learned:
✅ {learning_1}
✅ {learning_2}
✅ {learning_3}

What challenged me: {challenge}

How I overcame it: {solution}

Progress, not perfection! 💪

#DataScience #MachineLearning #LearningInPublic #WeekInReview""",
        
        "project_progress": """Project Update: {project_name}

Progress this week: {progress}

Key insight: {insight}

Tools used: {tools}

Next steps: {next_steps}

Follow along for more updates!

#DataScience #MachineLearning #Portfolio #Python""",
        
        "reflection": """3 things I learned this week in Data Science:

1️⃣ {insight_1}

2️⃣ {insight_2}

3️⃣ {insight_3}

To everyone starting their DS journey: be patient with yourself. Progress compounds.

What did you learn this week? Share below!

#DataScience #CareerAdvice #Learning #StudentLife"""
    }
    
    def __init__(self, data_file: str = 'linkedin_content.json'):
        self.data_file = data_file
        self.content_bank = self._load_content_bank()
    
    def _load_content_bank(self) -> Dict:
        """Load or create content bank"""
        if Path(self.data_file).exists():
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {
            'posts': [],
            'ideas': [],
            'templates': list(self.TEMPLATES.keys()),
            'stats': {
                'total_posts': 0,
                'posts_this_week': 0,
                'followers_gained': 0
            }
        }
    
    def _save_content_bank(self):
        """Save content bank to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.content_bank, f, indent=2)
    
    def add_daily_learning(self, topic: str, key_learning: str, 
                          application: str, personal_insight: str,
                          day_number: int = 1) -> str:
        """
        Create a LinkedIn post from daily learning
        
        Args:
            topic: What you learned today (e.g., "Gradient Descent")
            key_learning: Brief explanation of the concept
            application: Real-world application
            personal_insight: Your personal take/question
            day_number: Day number of your learning journey
        
        Returns:
            Formatted LinkedIn post
        """
        post = self.TEMPLATES["ml_concept"].format(
            day=day_number,
            topic=topic,
            explanation=key_learning,
            application=application,
            personal_insight=personal_insight
        )
        
        # Save to content bank
        self.content_bank['posts'].append({
            'date': datetime.now().isoformat(),
            'template': 'ml_concept',
            'content': post,
            'topic': topic
        })
        self.content_bank['stats']['total_posts'] += 1
        self._save_content_bank()
        
        return post
    
    def add_code_tip(self, topic: str, problem: str, 
                     solution: str, explanation: str) -> str:
        """
        Create a code tip post
        
        Args:
            topic: What the tip is about
            problem: The problem it solves
            solution: The code or solution
            explanation: Why it works
        """
        post = self.TEMPLATES["code_tip"].format(
            topic=topic,
            problem=problem,
            solution=solution,
            explanation=explanation
        )
        
        self.content_bank['posts'].append({
            'date': datetime.now().isoformat(),
            'template': 'code_tip',
            'content': post,
            'topic': topic
        })
        self.content_bank['stats']['total_posts'] += 1
        self._save_content_bank()
        
        return post
    
    def add_weekly_update(self, week: int, topic: str,
                         learnings: List[str], challenge: str,
                         solution: str) -> str:
        """
        Create a weekly learning update
        
        Args:
            week: Week number
            topic: Main topic of the week
            learnings: List of 3 key learnings
            challenge: What challenged you
            solution: How you overcame it
        """
        post = self.TEMPLATES["weekly_update"].format(
            week=week,
            topic=topic,
            learning_1=learnings[0],
            learning_2=learnings[1],
            learning_3=learnings[2],
            challenge=challenge,
            solution=solution
        )
        
        self.content_bank['posts'].append({
            'date': datetime.now().isoformat(),
            'template': 'weekly_update',
            'content': post,
            'topic': topic
        })
        self.content_bank['stats']['total_posts'] += 1
        self._save_content_bank()
        
        return post
    
    def add_project_update(self, project_name: str, progress: str,
                          insight: str, tools: str, next_steps: str) -> str:
        """
        Create a project progress update
        
        Args:
            project_name: Name of your project
            progress: What you accomplished
            insight: Key insight discovered
            tools: Tools/technologies used
            next_steps: What's coming next
        """
        post = self.TEMPLATES["project_progress"].format(
            project_name=project_name,
            progress=progress,
            insight=insight,
            tools=tools,
            next_steps=next_steps
        )
        
        self.content_bank['posts'].append({
            'date': datetime.now().isoformat(),
            'template': 'project_progress',
            'content': post,
            'topic': project_name
        })
        self.content_bank['stats']['total_posts'] += 1
        self._save_content_bank()
        
        return post
    
    def add_reflection(self, insights: List[str]) -> str:
        """
        Create a reflection post with 3 insights
        
        Args:
            insights: List of 3 insights from the week
        """
        post = self.TEMPLATES["reflection"].format(
            insight_1=insights[0],
            insight_2=insights[1],
            insight_3=insights[2]
        )
        
        self.content_bank['posts'].append({
            'date': datetime.now().isoformat(),
            'template': 'reflection',
            'content': post,
            'topic': 'Weekly Reflection'
        })
        self.content_bank['stats']['total_posts'] += 1
        self._save_content_bank()
        
        return post
    
    def save_post_idea(self, idea: str, category: str = "general"):
        """Save a post idea for later"""
        self.content_bank['ideas'].append({
            'date': datetime.now().isoformat(),
            'idea': idea,
            'category': category,
            'used': False
        })
        self._save_content_bank()
        print(f"✅ Idea saved: {idea[:50]}...")
    
    def get_post_ideas(self, category: Optional[str] = None) -> List[Dict]:
        """Get saved post ideas"""
        ideas = self.content_bank['ideas']
        if category:
            ideas = [i for i in ideas if i['category'] == category and not i['used']]
        return ideas
    
    def get_all_posts(self) -> List[Dict]:
        """Get all created posts"""
        return self.content_bank['posts']
    
    def get_stats(self) -> Dict:
        """Get posting statistics"""
        return self.content_bank['stats']
    
    def export_posts_to_txt(self, filename: str = 'linkedin_posts.txt'):
        """Export all posts to a text file for easy copying"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("LINKEDIN POSTS - Ready to Copy & Paste\n")
            f.write("=" * 60 + "\n\n")
            
            for i, post in enumerate(self.content_bank['posts'], 1):
                f.write(f"--- POST {i} ---\n")
                f.write(f"Date: {post['date'][:10]}\n")
                f.write(f"Topic: {post['topic']}\n")
                f.write(f"Template: {post['template']}\n\n")
                f.write(post['content'])
                f.write("\n\n" + "=" * 60 + "\n\n")
        
        print(f"✅ Posts exported to {filename}")
    
    def show_menu(self):
        """Interactive menu for creating posts"""
        print("\n" + "=" * 60)
        print("LINKEDIN CONTENT ORGANIZER FOR ML STUDENTS")
        print("=" * 60)
        print(f"Total posts created: {self.content_bank['stats']['total_posts']}")
        print("\nWhat would you like to do?")
        print("1. Create daily learning post")
        print("2. Create code tip post")
        print("3. Create weekly update")
        print("4. Create project update")
        print("5. Create reflection post")
        print("6. Save post idea for later")
        print("7. View saved ideas")
        print("8. Export all posts to file")
        print("9. View statistics")
        print("0. Exit")
        print("=" * 60)


def main():
    """Main interactive function"""
    organizer = LinkedInContentOrganizer()
    
    while True:
        organizer.show_menu()
        choice = input("\nEnter your choice (0-9): ").strip()
        
        if choice == '1':
            print("\n--- Daily Learning Post ---")
            day = input("Day number: ")
            topic = input("Topic (e.g., 'Gradient Descent'): ")
            learning = input("What is it? (1-2 sentences): ")
            application = input("Real-world application: ")
            insight = input("Your personal take: ")
            
            post = organizer.add_daily_learning(
                topic=topic,
                key_learning=learning,
                application=application,
                personal_insight=insight,
                day_number=int(day) if day else 1
            )
            print("\n" + "=" * 60)
            print("YOUR LINKEDIN POST:")
            print("=" * 60)
            print(post)
            print("=" * 60)
        
        elif choice == '2':
            print("\n--- Code Tip Post ---")
            topic = input("Tip topic: ")
            problem = input("Problem it solves: ")
            solution = input("Solution (code or explanation): ")
            explanation = input("Why it works: ")
            
            post = organizer.add_code_tip(topic, problem, solution, explanation)
            print("\n" + "=" * 60)
            print("YOUR LINKEDIN POST:")
            print("=" * 60)
            print(post)
            print("=" * 60)
        
        elif choice == '3':
            print("\n--- Weekly Update ---")
            week = input("Week number: ")
            topic = input("Main topic: ")
            learnings = [
                input("Learning 1: "),
                input("Learning 2: "),
                input("Learning 3: ")
            ]
            challenge = input("What challenged you: ")
            solution = input("How you overcame it: ")
            
            post = organizer.add_weekly_update(
                week=int(week),
                topic=topic,
                learnings=learnings,
                challenge=challenge,
                solution=solution
            )
            print("\n" + "=" * 60)
            print("YOUR LINKEDIN POST:")
            print("=" * 60)
            print(post)
            print("=" * 60)
        
        elif choice == '4':
            print("\n--- Project Update ---")
            name = input("Project name: ")
            progress = input("Progress this week: ")
            insight = input("Key insight: ")
            tools = input("Tools used: ")
            next_steps = input("Next steps: ")
            
            post = organizer.add_project_update(
                project_name=name,
                progress=progress,
                insight=insight,
                tools=tools,
                next_steps=next_steps
            )
            print("\n" + "=" * 60)
            print("YOUR LINKEDIN POST:")
            print("=" * 60)
            print(post)
            print("=" * 60)
        
        elif choice == '5':
            print("\n--- Reflection Post ---")
            insights = [
                input("Insight 1: "),
                input("Insight 2: "),
                input("Insight 3: ")
            ]
            
            post = organizer.add_reflection(insights)
            print("\n" + "=" * 60)
            print("YOUR LINKEDIN POST:")
            print("=" * 60)
            print(post)
            print("=" * 60)
        
        elif choice == '6':
            print("\n--- Save Post Idea ---")
            idea = input("Your idea: ")
            category = input("Category (ml/python/visualization/etc): ")
            organizer.save_post_idea(idea, category)
        
        elif choice == '7':
            print("\n--- Saved Ideas ---")
            ideas = organizer.get_post_ideas()
            if ideas:
                for i, idea in enumerate(ideas, 1):
                    print(f"{i}. [{idea['category']}] {idea['idea'][:60]}...")
            else:
                print("No saved ideas yet.")
        
        elif choice == '8':
            filename = input("Filename (default: linkedin_posts.txt): ") or 'linkedin_posts.txt'
            organizer.export_posts_to_txt(filename)
        
        elif choice == '9':
            print("\n--- Statistics ---")
            stats = organizer.get_stats()
            print(f"Total posts created: {stats['total_posts']}")
            print(f"Posts in content bank: {len(organizer.content_bank['posts'])}")
            print(f"Saved ideas: {len(organizer.content_bank['ideas'])}")
        
        elif choice == '0':
            print("\nGoodbye! Keep learning and posting! 🚀")
            break
        
        else:
            print("\nInvalid choice. Please try again.")


# Example usage for quick posts
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--example':
        # Run example
        organizer = LinkedInContentOrganizer()
        
        # Example: Create a post about NumPy
        post = organizer.add_daily_learning(
            topic="NumPy Arrays vs Python Lists",
            key_learning="NumPy arrays are up to 50x faster than Python lists because they store data in contiguous memory blocks",
            application="This is why Scikit-learn uses NumPy arrays as its fundamental data structure for ML models",
            personal_insight="I never realized how much performance matters until I started working with larger datasets!",
            day_number=1
        )
        print("Example post created!")
        print(post)
        
        # Export all posts
        organizer.export_posts_to_txt()
    else:
        # Run interactive menu
        main()