# Tool Archive

This folder keeps retired, campaign-specific utilities available for reference without crowding the active `tools/` directory.

- `campaign-one-offs/` — scripts made for completed campaigns or a specific production batch.
- `klaviyo-reference/` — examples and reference-only Klaviyo code. These scripts are not part of the current deployment workflow.

For normal campaign work, use the active tools in the parent directory:

- `build_campaign_html.py` — build an email HTML file from a base template and replacements.
- `klaviyo_create_template.py` — create a Klaviyo template from local HTML.
- `klaviyo_deploy_campaign.py` — create a template and campaign, then assign the template.

The active Klaviyo tools read `KLAVIYO_API_KEY` from the repository `.env` file.
