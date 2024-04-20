def format_abstract_prompt(invention_disclosure, prior_art):
    return f"""
    You have been asked to write an abstract for a patent application.

    The invention disclosure is as follows:
    {invention_disclosure}

    The prior art is as follows:
    {prior_art}

    Write an abstract for this patent application.

    Do not return any text other than the abstract.

    Return your results with a markdown header "## Abstract".
    """

def format_plan_specification_prompt(abstract, invention_disclosure, prior_art):
    return f"""
    You have been asked to write a patent application for the following invention:

    Abstract:
    {abstract}

    Invention Disclosure:
    {invention_disclosure}

    Prior Art:
    {prior_art}

    You are to write a plan for the patent specification. Each of these sections will then be written separately.

    Return your response as a list of strings, where each string is a section of the plan.
    """

def format_specification_prompt(section, patent, invention_disclosure, prior_art):
    return f"""
    You have been asked to write a patent application for the following invention:

    Invention Disclosure:
    {invention_disclosure}

    Prior Art:
    {prior_art}

    You are to write the following section of the patent specification:
    {section}

    So far, the patent application looks like this:
    {patent}

    Write the section of the patent specification.

    Do not return any text other than the section of the patent specification.

    Return your results with a markdown header (e.g. "## Background").
    """

def format_claims_prompt(patent, invention_disclosure, prior_art):
    return f"""
    You have been asked to write a patent application for the following invention:

    Invention Disclosure:
    {invention_disclosure}

    Prior Art:
    {prior_art}

    You are to write the claims section of the patent specification.

    So far, the patent application looks like this:

    {patent}

    Write the claims section of the patent specification.

    Do not return any text other than the claims.

    Return your results with a markdown header "## Claims".
    """
