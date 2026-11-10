from django import template
from django.utils.safestring import mark_safe
import markdown as md_lib
import re

register = template.Library()

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def render_markdown(value):
    """
    Renders markdown content to clean HTML while preserving LaTeX math blocks ($...$ and $$...$$).
    """
    if not value:
        return ""

    placeholders = {}

    def repl_display(m):
        key = f"XYZMATHDISP{len(placeholders)}XYZ"
        placeholders[key] = m.group(0)
        return key

    def repl_inline(m):
        key = f"XYZMATHINL{len(placeholders)}XYZ"
        placeholders[key] = m.group(0)
        return key

    # 1. Protect display math $$ ... $$
    text = re.sub(r'\$\$(.+?)\$\$', repl_display, value, flags=re.DOTALL)
    
    # 2. Protect inline math $ ... $
    text = re.sub(r'\$([^\$\n]+?)\$', repl_inline, text)

    # 3. Convert markdown to HTML
    html = md_lib.markdown(
        text,
        extensions=[
            'extra',
            'tables',
            'fenced_code',
            'sane_lists'
        ]
    )

    # 4. Restore LaTeX math blocks
    for key, val in placeholders.items():
        html = html.replace(key, val)

    return mark_safe(html)

@register.filter
def render_manuscript(value):
    """
    Renders manuscript body, stripping duplicate leading H1 and blockquote premise
    since they are prominently displayed in the manuscript header banner.
    """
    if not value:
        return ""
    # Strip leading H1 title
    clean_val = re.sub(r'^\s*#[^#\n]+?\n+', '', value)
    # Strip leading blockquote
    clean_val = re.sub(r'^\s*>[^\n]*?\n+(\s*>[^\n]*?\n+)*', '', clean_val)
    # Strip leading horizontal rule
    clean_val = re.sub(r'^\s*---\s*\n+', '', clean_val)
    return render_markdown(clean_val)

@register.filter
def render_definition(value):
    """
    Renders a topic definition or summary cleanly with Markdown and LaTeX math support,
    ensuring no raw heading markers or broken markup appear.
    """
    if not value:
        return ""
    # Strip any leading blockquote markers or Definition: labels if passed raw
    clean_val = re.sub(r'^\s*>\s*(?:\*\*)?(?:Formal\s+)?Definition:?(?:\*\*)?\s*', '', value, flags=re.IGNORECASE)
    clean_val = re.sub(r'^\s*#+[^\n]*\n*', '', clean_val)
    return render_markdown(clean_val)

@register.filter
def format_headers(value):
    """
    Alias for backward compatibility.
    """
    return render_markdown(value)
