import axios from "axios"
const URL = "http://localhost:8080";

const getUsers = async () => {
  try {
    const res = await axios.get(`${URL}/users`);
    return res.data;
  } catch (e) {
    return { message: e.message };
  }
};

const postUser = async (firstName, lastName, idNumber) => {
  try {
    const res = await axios.post(`${URL}/users`, {
        firstName,
        lastName,
        idNumber,
      })
    return res.data;
  } catch (e) {
    return e;
  }
};

export {
  getUsers,
  postUser,
};
