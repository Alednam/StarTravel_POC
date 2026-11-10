from django.db import models
import re

class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    simulation_logic = models.TextField(blank=True, help_text="4PT/Simulation-specific interpretation of this topic.")
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.course.name} - {self.name}"

    @property
    def definition(self):
        """
        Extracts the formal definition or concise summary of the topic.
        If topic.content contains a blockquote definition (`> **Formal Definition:** ...` or `> **Definition:** ...`),
        it extracts that text. Otherwise, it strips leading headers and formats
        the first substantive paragraph.
        """
        if not self.content:
            return ""
        
        # 1. Check for explicit blockquote definition: > **Formal Definition:** text or > **Definition:** text
        m = re.search(r'>\s*(?:\*\*)?(?:Formal\s+)?Definition:?(?:\*\*)?\s*(.+?)(?=\n\s*\n|\n\s*#|$)', self.content, re.DOTALL | re.IGNORECASE)
        if m:
            raw_def = m.group(1).replace('\n>', ' ').replace('\n', ' ').strip()
            return raw_def
        
        # 2. Fallback: Strip headers and extract first substantive paragraph
        clean = re.sub(r'^\s*#+[^\n]*\n+', '', self.content)
        paras = [p.strip() for p in clean.split('\n\n') if p.strip() and not p.strip().startswith('#') and not p.strip().startswith('$$')]
        if paras:
            first_para = paras[0].replace('\n', ' ')
            return first_para
        return ""

class Equation(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='equations')
    name = models.CharField(max_length=200)
    formula = models.CharField(max_length=500) # LaTeX or Sympy string
    explanation = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Theory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    premise = models.TextField(blank=True)
    is_sealed = models.BooleanField(default=False)
    content_hash = models.CharField(max_length=64, blank=True)
    
    # Relationships
    topics = models.ManyToManyField(Topic, related_name='theories', blank=True)
    
    # Granular data (stored as JSON for flexibility, or separate fields)
    axioms = models.JSONField(default=list, blank=True)
    mechanisms = models.JSONField(default=list, blank=True)
    domains = models.JSONField(default=list, blank=True)
    gaps = models.JSONField(default=list, blank=True)
    definitions = models.JSONField(default=list, blank=True)
    
    # Mathematical Physics extensions
    symmetries = models.JSONField(default=list, blank=True)
    invariants = models.JSONField(default=list, blank=True)
    equations_list = models.JSONField(default=list, blank=True)
    empirical_benchmarks = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name
