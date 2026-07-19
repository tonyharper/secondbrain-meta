<!-- Source: https://fb.workplace.com/groups/1167810663557228/permalink/2576711872667093/ -->
<!-- Title: Launch Post — Launching: Risk Data SEVs and SEV Reviews -->
<!-- Author: Tony Harper -->
<!-- Date posted: 2025-06-16 -->
<!-- Date accessed: 2026-03-31 -->

# Launching: Risk Data SEVs and SEV Reviews

In order to improve the Resilience and Quality of Risk data, starting today Risk DE will be implementing a Risk Analytics-wide SEV process. This includes initial SEV guidelines for key datasets as well as SEV reviews and an IMOC rotation.

## What does this mean for me?

We are focusing on key datasets. These are datasets that, if we get them wrong, are important enough to negatively impact the strategy of the Risk organization and/or reporting to our external stakeholders.

As we begin this process, these datasets will be determined by each oncall, with help from our SEV IMOCs as needed. Over time, we will build programmatic methods of identifying and monitoring these datasets.

**If you are an owner or oncall for one of these datasets**, then you will be expected to follow the SEV process. (For a note on why SEVs matter, [read this](https://fb.workplace.com/groups/414072651974689/permalink/1974819302566675/).)

## Incident Response

In addition to creating SEV guidelines and a SEV review, we are also introducing a Data Engineering IMOC rotation. IMOC stands for Incident Manager OnCall. The job of the IMOC is as follows:

- Make sure that the right people are working on the SEV and prioritizing the work to drive it to resolution
- Make sure that the work is being communicated out in a timely manner
- Make sure that critical decisions are made once the relevant information is presented

The IMOC is not in this alone -- we will build a group of senior DEs who will help each other to make the decisions here, especially in the early days of this process.

Additionally -- **the IMOC's job is not to resolve the SEV, but to ensure that it gets on the path to resolution.**

### IMOC Details

- US Timezone: [risk_data_imoc](https://www.internalfb.com/omh/view/risk_data_imoc)
- UK Timezone: risk_data_imoc_lon

## How Do I File a SEV?

We are launching with manual SEV reporting; over time we will build automation, though manual reports are always welcome. Please use the following steps to ensure accurate and efficient SEV reporting and management:

1. **Identify Delays or Quality issues in Key Tables and Metrics:**
   - If a key table (use your best judgement and connect with the TL or SME for that artifact) experiences a delay exceeding 24 hours or is reporting substantially inaccurate values, promptly notify the Incident Manager on Call (IMOC) via chat. Include the following details:
     - Artifact Name: Specify whether it is a Table or Dashboard.
     - Data Issue: Clearly describe the nature of the issue, such as SLO breach (data delays), data quality concerns, or data inconsistency.

2. **SEV Level Determination:**
   - The IMOC will evaluate the provided information to determine the appropriate SEV level.

3. **SEV Creation and Collaboration:**
   - The IMOC will initiate the SEV creation process and collaborate with the person who reported the issue to gather any additional information necessary for comprehensive SEV documentation.

4. **Stakeholder Engagement:**
   - Both the IMOC and the reporter will ensure that relevant stakeholders are added to the SEV chat. This step is crucial for facilitating effective communication and engagement from key personnel involved in the resolution process.

We aim to ensure that all SEVs are reported and addressed in a timely and organized manner. Your cooperation and attention to detail in this manual process are greatly appreciated as we work towards a more automated solution.

## Types of SEVs

Data SEVs fall into 3 categories:

- **SLO SEVs:** Your data is late. Timely data is critical and making sure that there is clear communication around SLA misses as well as follow ups to prevent them in the future is important to making sure that we are able to provide data in a timely manner.
- **Data Quality SEVs:** Your data is inaccurate. Accurate data is very important. See [this note](https://fb.facebook.com/notes/will-laves/inaccurate-data-in-key-tables/1131326000351624/?fref=mentions) to understand which steps to take when you find that you have published inaccurate data, including filing a SEV.
- **Data Inconsistency SEVs:** Data points that should match should always match. If two different datasets contain the same metric, they should agree. If they do not, then we need to figure out why they don't match, and how to fix it.

## SEV Reviews

SEV reviews are how we get better as an org. Every time something goes wrong, we can figure out how to make sure that it doesn't go wrong again. Sometimes this will be simple fixes and other times we may come up with more scalable solutions. By seeing where the gaps are and reviewing all of them, we can come up with creative and scalable solutions which will make the entire data warehouse better.

We will schedule monthly SEV reviews starting in late June 2025. We will publish the outcomes from each SEV review after it concludes.

## How can I be more involved?

First, help your team adopt the upcoming SEV guidelines.

If you would like to be more involved in the working group, IMOC rotation, or the SEV reviews themselves, please talk to your manager.
