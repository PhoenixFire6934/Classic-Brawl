from Packets.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.Login.LoginMessage import LoginMessage
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage
from Packets.Messages.Client.Gameroom.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.Gameroom.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.Home.AskProfileMessage import AskProfileMessage
from Packets.Messages.Client.Gameroom.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.Gameroom.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.AnalyticsEventMessage import AnalyticsEventMessage
from Packets.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Packets.Messages.Client.SetNameMessage import SetNameMessage
from Packets.Messages.Client.Home.GetLeaderboardMessage import GetLeaderboardMessage
from Packets.Messages.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Packets.Messages.Client.Gameroom.TeamSetRankedLocationMessage import TeamSetRankedLocationMessage
from Packets.Messages.Client.Home.PlayerStatusMessage import PlayerStatusMessage
from Packets.Messages.Client.ClientCapabilities import ClientCapabilities
from Packets.LogicCommandManager import EndClientTurn
from Packets.Messages.Client.Battle.Cancel_Matchmaking import CancelMatchMaking
from Packets.Messages.Client.Battle.OnPlay import OnPlay

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

# Friend
from Packets.Messages.Client.Friend.AddFriend import AddFriend
from Packets.Messages.Client.Friend.AskForFriendListMessage import AskForFriendListMessage
from Packets.Messages.Client.Friend.AskForFriendSuggestionsMessage import AskForFriendSuggestionsMessage
from Packets.Messages.Client.Friend.FacebookConnect import FacebookConnect
from Packets.Messages.Client.Friend.UnlinkFacebookAcount import UnlinkFacebookAcount

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10107: ClientCapabilities,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    10212: SetNameMessage,
    10502: AddFriend,
    10504: AskForFriendListMessage,
    10599: AskForFriendSuggestionsMessage,
    14102: EndClientTurn,
    14103: OnPlay,
    14106: CancelMatchMaking,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: AskProfileMessage,
    14201: FacebookConnect,
    14211: UnlinkFacebookAcount,

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

    # Friendly battle lobby
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14363: TeamSetLocationMessage,
    14354: TeamChangeMemberSettingsMessage,
    14362: TeamSetRankedLocationMessage,
    14363: TeamSetLocationMessage,
    14366: PlayerStatusMessage,

    14403: GetLeaderboardMessage,
    14600: AvatarNameCheckRequestMessage,
}