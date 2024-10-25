import axios from '@/libs/axios';
 
export function getJobListingData() {
    let endpoint = "/api/v1/report/?year=2024"
    let months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    let output = {
      applications_count_data: months.map(month => {
        return {
          name: month,
          job_listings: 0,
          applications: 0
        }
      })
    }
  
    months.forEach((month, index) => {
      axios.get(endpoint + "&month=" + (index+1))
      .then(function (response) {
          output.applications_count_data[index+1] = {
            name: months[index],
            job_listings: response.data.job_listings_amount,
            applications: response.data.applications_amount
          }
      }).catch(error => {
        console.log(error)
      })
    })
     
    console.log(output)
    return output
  }
  