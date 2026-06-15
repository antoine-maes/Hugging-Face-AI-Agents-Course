# Agent :

## Definition
- Comprends le langage naturel
- Peut disposer d'outils 
- Resonne et utilise ou non ses outils

## Types d'agents
Basique : Tu lui poses une question, il repond
Router : Il permet de classifier (chemin1 vs chemin2 sinon chemin3)
Tool Caller : Il determine quel outils utiliser 
Multi-step Agent : Orchestrateur, il determine si il faut continuer la boucle agentique
Multi-Agent : Il determine quel agent appeler 


Feature	Chain-of-Thought (CoT)	ReAct
Step-by-step logic	✅ Yes	✅ Yes
External tools	❌ No	✅ Yes (Actions + Observations)
Best suited for	Logic, math, internal tasks	Info-seeking, dynamic multi-step tasks