// schema
// https://github.com/pawlaczyk/MERN_stack_tutorial/blob/master/backend/models/workoutModel.js
const { Schema, model } = require("mongoose");

const noteSchema = new Schema({
  _id: String,
  data: Object,
  //   dopdatkowe pola do notatki
});

module.exports = model("Note", noteSchema);
