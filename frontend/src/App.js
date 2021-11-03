import React, { useState } from "react";
import { postUser, getUsers } from "./services/user.services";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [idNumber, setIdNumber] = useState("");
  const [alert, setAlert] = useState("danger");
  const [message, setMessage] = useState("");
  const [users, setUsers] = useState([]);

  const onChangeFirstName = ({ target: { value } }) => {
    setFirstName(value);
  };

  const onChangeLastName = ({ target: { value } }) => {
    setLastName(value);
  };

  const onChangeIdNumber = ({ target: { value } }) => {
    setIdNumber(value);
  };

  const getUsersHandler = async () => {
    try {
      const data = await getUsers();
      setUsers((prev) => [...data.data]);
    } catch (e) {
      console.log(e.message);
    }
  };

  const handleSubmit = async (e) => {
    try {
      e.preventDefault();
      const data = await postUser(firstName, lastName, idNumber);
      console.log(data);
      if (data.data) {
        setAlert("success");
        setMessage(data.data);
        setFirstName("");
        setLastName("");
        setIdNumber("");
      } else {
        setAlert("danger");
        setMessage(data.message);
      }
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <div className="App">
      <div className="row justify-content-center">
        <div className="col-sm-2">
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">First Name:</label>
              <input
                type="text"
                className="form-control"
                value={firstName}
                onChange={onChangeFirstName}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Last Name:</label>
              <input
                type="text"
                className="form-control"
                value={lastName}
                onChange={onChangeLastName}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Id Number:</label>
              <input
                type="text"
                className="form-control"
                value={idNumber}
                onChange={onChangeIdNumber}
              />
            </div>
            <div className="d-grid gap-2 block">
              <button className="btn btn-primary" type="submit">
                Submit
              </button>
              <button
                className="btn btn-dark"
                type="button"
                onClick={getUsersHandler}
              >
                Get users list:
              </button>
            </div>
            <div className={`alert alert-${alert} mt-2`} role="alert">
              {message}
            </div>
          </form>
        </div>
        <div className="col-sm-3">
          <h4>Users List:</h4>
          <ul className="list-group list-group-flush">
            {users.map((user, index) => (
              <li className="list-group-item" key={index}>
                <strong>FirstName:</strong> {user.firstName},{" "}
                <strong>LastName:</strong> {user.lastName},{" "}
                <strong>IdNumber:</strong> {user.idNumber}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;
