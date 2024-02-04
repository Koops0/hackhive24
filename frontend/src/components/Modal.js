import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Workout Log</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="workout-title">Log Title</Label>
              <Input
                type="text"
                id="workout-title"
                name="title"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Workout Log Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="workout-month">Month</Label>
              <Input
                type="text"
                id="workout-month"
                name="month"
                value={this.state.activeItem.month}
                onChange={this.handleChange}
                placeholder="Enter Month"
              />
            </FormGroup>
            <FormGroup>
              <Label for="workout-day">Day</Label>
              <Input
                type="text"
                id="workout-day"
                name="day_of_workout"
                value={this.state.activeItem.day_of_workout}
                onChange={this.handleChange}
                placeholder="Enter Day"
              />
            </FormGroup>
            <FormGroup>
              <Label for="workout-year">Year</Label>
              <Input
                type="text"
                id="workout-year"
                name="year"
                value={this.state.activeItem.year}
                onChange={this.handleChange}
                placeholder="Enter Year"
              />
            </FormGroup>
            <FormGroup>
              <Label for="workout-description">Description</Label>
              <Input
                type="text"
                id="workout-description"
                name="description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Workout Description for this log"
              />
            </FormGroup>
            <FormGroup check>
              <Label check>
                <Input
                  type="checkbox"
                  name="completed"
                  checked={this.state.activeItem.completed}
                  onChange={this.handleChange}
                />
                Completed
              </Label>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}