# Email Triage OpenEnv

## Description
Simulates email inbox management.

## Tasks
- Easy: Spam detection
- Medium: Priority classification
- Hard: Reply generation

## Action Space
- classification: spam/urgent/normal
- priority: 1–3
- reply: string

## Reward
0.0 – 1.0 based on correctness

## Setup
docker build .
docker run

## Baseline Score
~0.3
