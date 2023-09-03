import './Input.css'
import { useState } from 'react'
import axios from 'axios'
import swal from 'sweetalert';

function Input() {
  const [title, setTitle] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    const parameter = { title }

    axios
      .post('http://localhost:8080/recommend', parameter)
      .then((res) => {
        const data = res.data.data
        const output = `1: ${data.movie1}\n2: ${data.movie2}\n3: ${data.movie3}\n4: ${data.movie4}\n5: ${data.movie5}\n6: ${data.movie6}\n7: ${data.movie7}\n8: ${data.movie8}\n9: ${data.movie9}\n10: ${data.movie10}`
        swal(output)
        reset()
      })
      .catch((error) => alert(`Error: Try a different movie title`))
  }

  const reset = () => {
    setTitle('')
  }

  return (
    <div className="glass">
      <form onSubmit={(e) => handleSubmit(e)} className="glass__form">
        <h4>Movie Recommendations</h4>
        <div className="glass__form__group">
          <input
            id="title"
            className="glass__form__input"
            placeholder="Input Movie Title: (ex. The Matrix, X-Men, The Fast and the Furious) "
            required
            autoFocus
            title="Title must be:"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>

        <div className="glass__form__group">
          <button type="submit" className="glass__form__btn">
            Submit
          </button>
        </div>
      </form>
    </div>
  )
}

export default Input