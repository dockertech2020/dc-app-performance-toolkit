from util.api.abstract_clients import RestClient


class FavfjsmClient(RestClient):

    def enable_plugin_for_project(self, project_id):
        print(f"Enabling plugin for project '{project_id}'...")

        api_url = f"{self.host}/plugins/servlet/favfjsd/config"
        form_data = {
            "projectId": project_id,
            "enable": True
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            self.post(api_url, f"Failed to enable plugin for project: {project_id}", body=form_data,
                      headers=headers, is_form_data=True, allow_redirect=True)
        except Exception as e:
            response_message = str(e)
            if "Project already has Feedback and Voting for Jira Service Management enabled" in response_message:
                print(f"Plugin already enabled for project '{project_id}'. Skipping...")
            else:
                raise e

    def configure_general_settings_for_project(self, project_id):
        print(f"Configuring general settings for project '{project_id}'...")

        api_url = f"{self.host}/rest/favfjsd/latest/config/projectconfig?projectId={project_id}"
        payload = {
            "isAdminNotified": True,
            "issueFilterType": "jql",
            "issueTypes": [],
            "jql": f"project = \"{project_id}\"",
            "portalLinkText": "Give feedback",
            "title": "Feedback & Voting for Jira Service Management",
            "votingSystem": "thumbs"
        }
        self.post(api_url, f"Failed to configure general settings for project: {project_id}", body=payload)

    def configure_permissions_for_project(self, project_id):
        print(f"Configuring general permissions for project '{project_id}'...")
        general_permissions_api_url = f"{self.host}/rest/favfjsd/latest/config/general-permissions?projectId=" \
                                      f"{project_id}"
        general_permissions_payload = {
            "checked": True,
            "option": "portalAccessAllowed"
        }
        self.post(general_permissions_api_url,
                  f"Failed to set permission to allow all customers with portal access to provide feedback",
                  body=general_permissions_payload)

        print(f"Configuring project permissions for project '{project_id}'...")
        project_permissions_api_url = f"{self.host}/rest/favfjsd/latest/config/project-permissions?projectId=" \
                                      f"{project_id}"
        project_permissions_payload = [
            # Service Desk Team
            {
                "projectRoleId": "10101",
                "viewPermissions": [
                    {
                        "permissionName": "agentview",
                        "toggled": True
                    },
                    {
                        "permissionName": "portalview",
                        "toggled": True
                    }
                ]
            },
            # Service Desk Customers
            {
                "projectRoleId": "10100",
                "viewPermissions": [
                    {
                        "permissionName": "agentview",
                        "toggled": False
                    },
                    {
                        "permissionName": "portalview",
                        "toggled": True
                    }
                ]
            },
            # Developers
            {
                "projectRoleId": "10102",
                "viewPermissions": [
                    {
                        "permissionName": "agentview",
                        "toggled": False
                    },
                    {
                        "permissionName": "portalview",
                        "toggled": False
                    }
                ]
            },
            # Administrators
            {
                "projectRoleId": "10002",
                "viewPermissions": [
                    {
                        "permissionName": "agentview",
                        "toggled": True
                    },
                    {
                        "permissionName": "portalview",
                        "toggled": True
                    }
                ]
            }
        ]
        self.post(project_permissions_api_url, f"Failed to configure project permissions for project: {project_id}",
                  body=project_permissions_payload)
