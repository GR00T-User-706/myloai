# MyLoAI Control Center Future Plans

> **Status:** Future planning only. None of the features in this document are part of the current implementation unless explicitly marked otherwise.

## Product direction

MyLoAI Control Center is a graphical-first frontend for interacting with configurable local and remote AI/LLM service providers.

The current product remains GUI-only. No command-line interface is required for the current release or for the repository migration.

A future CLI may be added later as a **control and initialization interface for MyLoAI**, not as a compatibility layer for a pre-existing MyLoAI CLI.

## Future configuration / initialization CLI

A future CLI may expose the same underlying configuration and control operations currently performed through the GUI.

Potential responsibilities include:

- initialize a new MyLoAI configuration;
- select or configure a provider;
- configure local or remote endpoints;
- select a default model;
- configure application-level settings;
- enable or configure plugins;
- create or select profiles;
- inspect current configuration;
- launch or attach to a configured MyLoAI session.

The goal would be reproducible, scriptable setup rather than duplicating the GUI as a second product.

A future initialization flow could conceptually look like:

```text
myloai init
  -> provider
  -> endpoint
  -> model
  -> plugins
  -> application settings
  -> save configuration
  -> optionally launch MyLoAI Control Center
```

The exact command surface is intentionally undefined. Do not implement a large CLI command taxonomy merely because the possibility exists.

## MyLoAI Conference Chat

A future feature concept is a multi-participant conference chat in which:

- the human user participates as a first-class participant;
- multiple LLM instances can participate in the same conversation;
- participants may use different providers;
- participants may use different models;
- local and remote providers may be mixed;
- each participant has an independent identity, provider, model, and configuration;
- all participants share the conversation context appropriate to the conference;
- the user can interrupt or stop generation immediately.

### Core problem

Ordinary chat uses a simple turn sequence:

```text
user -> model -> user -> model -> ...
```

A conference cannot safely use an unrestricted:

```text
AI -> AI -> AI -> AI -> AI -> ...
```

loop because participants could continue responding to one another indefinitely while the user is effectively locked out.

### Required future turn scheduler

Conference Chat therefore requires an explicit turn-management system.

Possible model:

```text
Participant queue
      |
      v
choose next participant
      |
      v
generate response
      |
      v
yield control
      |
      +--> user interruption
      +--> next participant
      +--> moderator/system rule
      +--> conference stop
```

The scheduler should be responsible for:

- turn order;
- participant eligibility;
- maximum consecutive turns;
- user priority;
- generation cancellation;
- conference stop/pause;
- participant timeout/error handling;
- preventing runaway AI-to-AI loops;
- optionally requiring user approval before another participant responds.

### Global interrupt

Conference Chat must have an immediate global interrupt mechanism.

Its semantic purpose is:

```text
STOP ALL ACTIVE GENERATION
CLEAR PENDING TURN EXECUTION
RETURN CONTROL TO USER
```

This must cancel active provider requests where the provider supports cancellation and must prevent queued participants from starting after the interrupt.

### Future conference policies

Potential scheduling policies include:

- strict round-robin;
- user-priority round-robin;
- moderator-selected next participant;
- mention/target based turns;
- maximum consecutive turns per participant;
- explicit handoff between participants;
- user approval between AI turns;
- time/token budgets per participant.

These are design possibilities, not current behavior.

## Provider architecture

The conference concept should build on the existing provider abstraction rather than hard-code Ollama or any single remote service.

A conference participant should conceptually reference:

```text
Participant
  ├── provider
  ├── endpoint
  ├── model
  ├── credentials/profile
  ├── generation parameters
  └── participant policy
```

This allows a future conference to combine multiple local and remote provider endpoints in one conversation.

The exact provider list should be derived from implemented backend adapters. Do not claim provider support that the code does not actually implement.

## Identity rule

The active MyLoAI repository is being consolidated under one application identity:

**MyLoAI Control Center**

The active codebase should use the canonical MyLoAI identity consistently. Legacy names such as `MyLoAI`, `myloai`, and `myloai` belong to historical context only unless a future migration document explicitly needs to refer to the old project.

## Non-goals for the current migration

The following are explicitly deferred:

- implementing the configuration CLI;
- implementing `myloai init`;
- implementing Conference Chat;
- implementing multi-agent turn scheduling;
- adding automatic AI-to-AI conversations;
- expanding the provider matrix without corresponding backend implementations;
- designing a full CLI command hierarchy.

The current migration is focused on producing a clean, coherent MyLoAI Control Center codebase and packaging ecosystem.
