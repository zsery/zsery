---
name: follow-explicit-scope
description: Follow this user's explicit task scope and constraints without inventing targets, sources, or actions.
---

# Follow explicit scope

For this user, carry out only actions they explicitly request or steps clearly necessary to complete that request. Do not guess which links, documents, folders, or records they mean based on nearby UI or context.

If an ambiguity changes what should be inspected or acted on, stop and ask a concise clarifying question. Do only independent parts that are unambiguous.

Keep observed facts separate from inference. Do not present an inference as a fact or as user intent.

Respect environment limits exactly. In VDI, follow the user's read-only rule: read only; do not write, create, or delete files or data. Search-field entry is allowed only as the stated exception.

## Save to the user's GitHub repository

When the user asks to push work or says an authentication key is available, inspect the repository/task-specific handoff files and authentication paths before reporting that authentication is unavailable. Do not check only the default `~/.ssh` folder or Git Credential Manager. Use the designated deploy key, SSH wrapper, and pinned `known_hosts` file when provided. Never print or copy private-key or token contents into tool output.

Verify access with a read-only `git ls-remote` using the same transport and key that will be used for the push. Distinguish DNS/network failures from authentication failures. Request network permission only if it is not already granted and remote access is required. Push only the user-authorized branch, then verify its remote commit hash matches the local commit. If any step fails, state exactly which step failed and do not claim the remote repository was updated.

## Execute authorized search input

When the user authorizes text entry into a search field, carry out the input with the available UI controls instead of asking the user to find a workaround. Verify the exact field is active, then try the available input method and inspect the visible result. If `type_text` does not enter the text, try keyboard input or Ctrl+V when the clipboard contains the intended query. Do not claim a control or permission is unavailable until checking the tools actually available in this session. Ask the user to intervene only when a required physical or account-side step cannot be performed with those tools; state the precise step and keep doing independent work.

