import Description from "./components/Description";
import Header from "./components/Header";
import Form from "./components/Form";

function App() {
  return (
      <div className="App">
          <Header/>
          <div className="content">
              <Description/>
              <Form/>
          </div>


      </div>
  );
}

export default App;
