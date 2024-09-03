module Main exposing (main)

import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick, onInput)
import Http
import Json.Encode as Encode
import Json.Decode exposing (Decoder, map3, field, int, string)

main =
  Browser.element
    { init = init
    , update = update
    , subscriptions = subscriptions
    , view = view
    }

type alias User =
  { name: String
  , email: String
  , jwt: String
  }

type alias Model =
  { email: String
  , password: String
  , user: Maybe User
  }

type Msg
  = Email String
  | Password String
  | Login
  | OnLogin (Result Http.Error User)

init : () -> (Model, Cmd Msg)
init _ = 
  (
    { email = ""
    , password = ""
    , user = Nothing
    }
  , Cmd.none
  )

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Email email ->
      ({ model | email = email }, Cmd.none)
    Password password ->
      ({ model | password = password }, Cmd.none)
    Login ->
      (model, Http.post { body = Http.jsonBody (loginEncoder model), url = "/login", expect = Http.expectJson OnLogin userDecoder })
    OnLogin result ->
      case result of
        Ok user ->
          ({model | user = Just user}, Cmd.none)
        Err _ ->
          ({model | email = "", password = ""}, Cmd.none)

subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none

view : Model -> Html Msg
view model =
  case model.user of
    Just user -> text user.email
    Nothing -> viewLogin model

viewLogin : Model -> Html Msg
viewLogin model =
  div []
    [
      input [type_ "text", placeholder "email", value model.email, onInput Email] []
    , input [type_ "password", placeholder "password", value model.password, onInput Password] []
    , button [onClick Login] [text "Login"]
    ]

loginEncoder: Model -> Encode.Value
loginEncoder model =
  Encode.object 
    [ ("email", Encode.string model.email)
    , ("password", Encode.string model.password)
    ]

userDecoder : Decoder User
userDecoder =
  map3 User
    (field "name" string)
    (field "email" string)
    (field "jwt" string)
