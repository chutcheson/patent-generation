# functions for patent generation
import json

from utils import generator
from writer_prompts import format_abstract_prompt, format_plan_specification_prompt, format_specification_prompt, format_claims_prompt


def generate_patent(invention_description, prior_art):
    patent = generate_abstract(invention_description, prior_art)
        
    """
    specification_plan = plan_specification(patent, invention_description, prior_art)

    for section in specification_plan:
        next_section = generate_specification(section, patent, invention_description, prior_art)
        patent += next_section
    """

    claims = generate_claims(patent, invention_description, prior_art)

    return patent + claims

def generate_abstract(invention_description, prior_art):
    abstract_prompt = format_abstract_prompt(invention_description, prior_art)
    abstract = generator(abstract_prompt)
    return abstract

def plan_specification(abstract, invention_description, prior_art):
    plan_specification_prompt = format_plan_specification_prompt(abstract, invention_description, prior_art)
    plan_specification = generator(plan_specification_prompt)
    return plan_specification

def generate_specification(section, patent, invention_description, prior_art):
    specification_prompt = format_specification_prompt(section, patent, invention_description, prior_art)
    specification = generator(specification_prompt)
    return specification

def generate_claims(specification, invention_description, prior_art):
    claims_prompt = format_claims_prompt(specification, invention_description, prior_art)
    claims = generator(claims_prompt)
    return claims


with open("invention_description.json", "r") as f:
    invention_description = json.load(f)

with open("prior_art.txt", "r") as f:
    #prior_art = f.readlines()
    prior_art = ""

generated_patent = generate_patent(invention_description, prior_art)

with open("generated_patent.txt", "w") as f:
    f.write(generated_patent)
