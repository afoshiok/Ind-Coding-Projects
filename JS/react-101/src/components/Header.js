import PropTypes from 'prop-types'

const Header = ({ title }) => {
  return (
    <header>
      <h1>{ title }</h1>
    </header>
  )
}

Header.defaultProps = {
  title: 'Task Tracker'
}

Header.propTypes = {
  title: PropTypes.string, //you can only pass strings into the title prop
}

//CSS in JS
// const headingStyle = {
//   color: 'red'
// }
export default Header
