import requests
from utils.helpers import save_to_csv

def fetch_user_roles(base_url, token):
    """Fetch all user roles."""
    url = f"{base_url}/api/userRoles?filter[is_editable]=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("data", [])

def fetch_permissions(base_url, token, user_role_id):
    """Fetch all permissions for a given user role."""
    headers = {"Authorization": f"Bearer {token}"}
    
    # Employee Actions
    employee_actions_url = f"{base_url}/api/userRoleEmployeeOptions/userRoleId/{user_role_id}"
    employee_actions = requests.get(employee_actions_url, headers=headers).json()

    # Data Group Permissions
    data_group_url = f"{base_url}/api/userRoleDataGroup/userRoleId/{user_role_id}"
    data_groups = requests.get(data_group_url, headers=headers).json()

    # Workflow Permissions
    workflow_url = f"{base_url}/api/userRoleWorkFlow/userRoleId/{user_role_id}"
    workflows = requests.get(workflow_url, headers=headers).json()

    return {
        "employee_actions": employee_actions,
        "data_groups": data_groups,
        "workflows": workflows
    }

def extract_permissions(base_url, token, output_file):
    """Extract permissions for all user roles and save to CSV."""
    user_roles = fetch_user_roles(base_url, token)
    all_permissions = []

    for role in user_roles:
        role_id = role["id"]
        role_name = role["name"]
        permissions = fetch_permissions(base_url, token, role_id)
        all_permissions.append({
            "Role Name": role_name,
            "Employee Actions": permissions["employee_actions"],
            "Data Groups": permissions["data_groups"],
            "Workflows": permissions["workflows"]
        })

    save_to_csv(all_permissions, output_file)
