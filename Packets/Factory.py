from Packets.Messages.Client.AnalyticsEventMessage import AnalyticsEventMessage
from Packets.CommandFactory import EndClientTurn
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage

# Login
from Packets.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.Login.LoginMessage import LoginMessage

# Gameroom
from Packets.Messages.Client.Gameroom.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.Gameroom.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.Gameroom.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.Gameroom.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.Gameroom.TeamUseGadgetMessage import TeamUseGadgetMessage
from Packets.Messages.Client.Gameroom.DoNotDistrubMessage import DoNotDistrubMessage

# Battle
from Packets.Messages.Client.Battle.BattleEndMessage import BattleEndMessage
from Packets.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage

# Home
from Packets.Messages.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Packets.Messages.Client.Home.AskProfileMessage import AskProfileMessage

# Player extra
from Packets.Messages.Client.SetNameMessage import SetNameMessage
from Packets.Messages.Client.SetContentCreatorMessage import SetContentCreatorMessage

# Alliances
from Packets.Messages.Client.Alliance.Create_Message import Create_Message
from Packets.Messages.Client.Alliance.Ask_Alliance_Data_Message import Ask_Alliance_Data_Message
from Packets.Messages.Client.Alliance.Ask_Joinable_Alliances_Message import Ask_Joinable_Alliances_Message
from Packets.Messages.Client.Alliance.Join_Message import Join_Message
from Packets.Messages.Client.Alliance.Promote_Alliance_Member_Message import Promote_Alliance_Member_Message
from Packets.Messages.Client.Alliance.Leave_Message import Leave_Message
from Packets.Messages.Client.Alliance.Chat_Message import Chat_Message
from Packets.Messages.Client.Alliance.Edit_Settings_Message import Edit_Settings_Message
# Join request
# Accept or decline request
# Invite member
from Packets.Messages.Client.Alliance.Search_Message import Search_Message

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    18686: SetContentCreatorMessage,
    10212: SetNameMessage,
    14102: EndClientTurn,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: BattleEndMessage,
    14113: AskProfileMessage,

    # Alliance
    14301: Create_Message,
    14302: Ask_Alliance_Data_Message,
    14303: Ask_Joinable_Alliances_Message,
    # 14304: Ask_Stream_Message,
    14305: Join_Message,
    14306: Promote_Alliance_Member_Message,
    # 14307: Kick_Member_Message,
    14308: Leave_Message,
    14315: Chat_Message,
    14316: Edit_Settings_Message,
    # 14317: Join_Request_Message,
    # 14321: Decide_Request_Message,
    # 14322: Invite_Member_Message,
    # 14323: Accept_Join_Invite_Message,
    14324: Search_Message,
    # 14330: Send_Club_Mail_Message,

    # Friendly battle lobby
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14363: TeamSetLocationMessage,
    14354: TeamChangeMemberSettingsMessage,
    14372: TeamUseGadgetMessage,

    14600: AvatarNameCheckRequestMessage,
    14777: DoNotDistrubMessage
}