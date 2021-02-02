from Packets.Messages.Client.Analytics_Event_Message import AnalyticsEventMessage
from Packets.CommandFactory import EndClientTurn
from Packets.Messages.Client.Keep_Alive_Message import KeepAliveMessage
from Packets.Messages.Client.Unknown import Unknown1

# Login
from Packets.Messages.Client.Login.Client_Hello_Message import ClientHelloMessage
from Packets.Messages.Client.Login.Login_Message import LoginMessage
from Packets.Messages.Client.Login.GetDeviceToken import GetDeviceToken

# Gameroom
from Packets.Messages.Client.Gameroom.Team_Create_Message import TeamCreateMessage
from Packets.Messages.Client.Gameroom.Team_Leave_Message import TeamLeaveMessage
from Packets.Messages.Client.Gameroom.Team_Set_Location_Message import TeamSetLocationMessage
from Packets.Messages.Client.Gameroom.TeamSetRankedLocationMessage import TeamSetRankedLocationMessage
from Packets.Messages.Client.Gameroom.Team_Change_Member_Settings_Message import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.Gameroom.Team_Use_Gadget_Message import TeamUseGadgetMessage
from Packets.Messages.Client.Gameroom.Do_Not_Distrub_Message import DoNotDistrubMessage

# Battle
from Packets.Messages.Client.Battle.Battle_End_Message import BattleEndMessage
from Packets.Messages.Client.Battle.Go_Home_From_Offline_Practise_Message import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.Battle.OnPlay import OnPlay
from Packets.Messages.Client.Battle.Cancel_Matchmaking import CancelMatchMaking

# Home
from Packets.Messages.Client.Home.Avatar_Name_Check_Request_Message import AvatarNameCheckRequestMessage
from Packets.Messages.Client.Home.Ask_Profile_Message import AskProfileMessage

# Leaderboard
from Packets.Messages.Client.Home.Get_Leaderboard_Message import GetLeaderboardMessage

# Player extra
from Packets.Messages.Client.Set_Name_Message import SetNameMessage
from Packets.Messages.Client.Set_Content_Creator_Message import SetContentCreatorMessage
from Packets.Messages.Client.ClientCapabilities import ClientCapabilities
from Packets.Messages.Client.Player.Player_State_Updated_Message import PlayerStateUpdatedMessage

# Alliances
from Packets.Messages.Client.Alliance.Create_Message import Create_Message
from Packets.Messages.Client.Alliance.Ask_For_Alliance_Data_Message import AskForAllianceDataMessage
from Packets.Messages.Client.Alliance.Ask_Joinable_Alliances_Message import Ask_Joinable_Alliances_Message
from Packets.Messages.Client.Alliance.Join_Message import Join_Message
from Packets.Messages.Client.Alliance.Promote_Alliance_Member_Message import Promote_Alliance_Member_Message
from Packets.Messages.Client.Alliance.Leave_Message import Leave_Message
from Packets.Messages.Client.Alliance.Alliance_Chat_Message import AllianceChatMessage
from Packets.Messages.Client.Alliance.Edit_Settings_Message import Edit_Settings_Message
# Join request
# Accept or decline request
# Invite member
from Packets.Messages.Client.Alliance.Search_Message import Search_Message
from Packets.Messages.Client.Alliance.Send_Club_Mail_Message import SendClubMail

# Friend
from Packets.Messages.Client.Friend.AddFriend import AddFriend
from Packets.Messages.Client.Friend.AskForFriendListMessage import AskForFriendListMessage
from Packets.Messages.Client.Friend.AskForFriendSuggestionsMessage import AskForFriendSuggestionsMessage
from Packets.Messages.Client.Friend.FacebookConnect import FacebookConnect
from Packets.Messages.Client.Friend.UnlinkFacebookAcount import UnlinkFacebookAcount

packets = {
    0: Unknown1,
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10107: ClientCapabilities,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    10113: GetDeviceToken,
    18686: SetContentCreatorMessage,
    10212: SetNameMessage,
    10502: AddFriend,
    10504: AskForFriendListMessage,
    10599: AskForFriendSuggestionsMessage,
    14102: EndClientTurn,
    14103: OnPlay,
    14106: CancelMatchMaking,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: BattleEndMessage,
    14113: AskProfileMessage,
    14201: FacebookConnect,
    14211: UnlinkFacebookAcount,
    14277: Unknown1,

    # Alliance
    14301: Create_Message,
    14302: AskForAllianceDataMessage,
    14303: Ask_Joinable_Alliances_Message,
    # 14304: Ask_Stream_Message,
    14305: Join_Message,
    14306: Promote_Alliance_Member_Message,
    # 14307: Kick_Member_Message,
    14308: Leave_Message,
    14315: AllianceChatMessage,
    14316: Edit_Settings_Message,
    # 14317: Join_Request_Message,
    # 14321: Decide_Request_Message,
    # 14322: Invite_Member_Message,
    # 14323: Accept_Join_Invite_Message,
    14324: Search_Message,
    14330: SendClubMail,

    # Friendly battle lobby
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14362: TeamSetRankedLocationMessage,
    14363: TeamSetLocationMessage,
    14366: PlayerStateUpdatedMessage,
    14372: TeamUseGadgetMessage,

    14403: GetLeaderboardMessage,
    14479: Unknown1,
    14600: AvatarNameCheckRequestMessage,
    14777: DoNotDistrubMessage
}