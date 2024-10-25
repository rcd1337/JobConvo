import axios from '@/libs/axios';
 
export async function signup(formData: FormData) {
  let endpoint = ""
  let payload: {[k: string]: any} = {
    account_data: {
      username: formData.get("name"),
      email: formData.get("email"),
      password: formData.get("password")
    }
  }

  if (formData.get("account_type") == "Recruiter") {
    payload.recruiter_profile_data = {
      company_name: formData.get("company")
    }
    payload.account_data.role = "Recruiter"
    endpoint = "/api/v1/register-recruiter/"
  }else if (formData.get("account_type") == "Applicant") {
    payload.account_data.role = "Applicant"
    payload.applicant_profile_data = {
      experience: formData.get("experience"),
      educational_level: formData.get("education"),
      salary_range_expectation: formData.get("salary")
    }
    endpoint = "/api/v1/register-applicant/"
  }

  axios.post(endpoint, payload).catch(error => {
    console.log(error)
  })
}

export async function signin(formData: FormData) {
  let endpoint = "/api/v1/token/"
  let payload = {
    email: formData.get("email"),
    password: formData.get("password")
  }

  axios.post(endpoint, payload)
  .then(function (response) {
    axios.defaults.headers["Authorization"] = "Bearer " + response.data.access
  }).catch(error => {
    console.log(error)
  })
}

