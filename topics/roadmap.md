# Qodana 2026 roadmap

<no-index/>

As of 2026, %product% continues to grow, and we would like to share our plans with you. 

This year should bring several new plugins, including an AI agent plugin, linter updates, and improvements to the existing functionalities of %product%. 

## AI agent plugin

Shipped as a separate plugin, the AI agent will be a part of the %product% ecosystem. This means that %product% script
will be used as an execution method, and it will support Grazie, BYOK, and LangFuse metrics.

## OpenGrep plugin for Qodana

This plugin is a fork of the original OpenGrep plugin that supports batch mode and local in-editor inspection.
It also includes a custom rules set handcrafted for SAST benchmarks, as well as Qodana approved profiles.

The plugin will be available on the [JetBrains Marketplace](https://plugins.jetbrains.com/).

## Safe-Code 

This plugin extends the security capabilities of the Rider IDE by providing a set of rules that can be used to detect 
and fix security issues. This is an OpenGrep plugin that includes some preselected OpenGrep rules, as well as a custom 
set of rules, detects hard-coded passwords, and provides the taint analysis capabilities for .NET and JavaScript.

## Code Provenance

Code Provenance is a new feature that lets you track the evolution of your code over time. It provides a detailed 
history of changes, including the ability to view the full history for each code change.

## Qodana for Rust

The Qodana for Rust linter is going to be bundled as per EAP version 2026.1 of %product%.
This linter will let you analyze Rust code using %product% capabilities, including the bundled %product%
plugin in [RustRover](https://www.jetbrains.com/help/rust/getting-started.html).

## Qodana for C/C++ release

Starting from 2026.1, the [%cpp%](clang.md) linter will be released from the EAP, which means more stability and 
performance improvements. 

## Edict dogfooding

This provides pipelines for ultimate commit and PR analysis, PR to ultimate branch, as well as a pipeline for 
applying and promoting generated inspections on quality gates and automated pipeline for applying feedback.





